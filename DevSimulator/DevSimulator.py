# -*- coding: utf-8 -*-
"""
purpose: DevSimulator
author: Haluk
date: 1/25/2018
"""
import io
import socket
import threading

import TcpServer

ADDR = '127.0.0.1'

class Dev:
    """
    __init__()
    constructs dev object.
    """
    def __init__(self):
        self.__portList = []
        self.__tcpServer = {}
        self.__lock = threading.Lock()
        self.__openingPFile = io.open('./OpenningPort','w')
        self.__idlePFile = io.open('./IdlePort','w')
    
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__portList.clear()
        self.__tcpServer.clear()
        self.__lock = None
        self.__openingPFile.close()
        self.__idlePFile.close()
        
    def IsPortOpenning(self,port):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
            s.connect((ADDR,port))
            s.shutdown(2)
            
            try:
                self.__lock.acquire()
                self.__openingPFile.write(ADDR+' '+str(port)+' is openning')
            except:
                pass;
            finally:
                self.__lock.release()
        except:
            try:
                self.__lock.acquire()
                self.__idlePFile.write(str(port)+'\n')
                self.__portList.append(port)
            except:
                pass;
            finally:
                self.__lock.release()
        
    def ScanfPort(self,beginPort,totalSize):
        begin = beginPort
        end = beginPort + totalSize
        for port in range(begin,end):
            thr = threading.Thread(target = self.IsPortOpenning,args = (port,))
            thr.start()
        
    def Run(self,beginPort,totalSize):
        self.ScanfPort(beginPort,totalSize)
        for i in self.__portList:
            self.__tcpServer[i] = TcpServer.TcpServer()
            thr = threading.Thread(target = self.__tcpServer[i].Init,args = (i,))
            thr.start()
    
if __name__ == '__main__':
    device = Dev()
    device.Run(1000,1000)
    
    while True:
        pass;