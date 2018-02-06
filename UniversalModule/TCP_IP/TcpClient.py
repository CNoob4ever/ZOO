# -*- coding: utf-8 -*-
"""
purpose: Client
author: Haluk
date: 1/25/2018
"""

import socket
import selectors
import struct
import Player

HEADER_SIZE = struct.calcsize('@2BI')
class TcpClient:
    """
    __init__()
    constructs tcp object.

    """
    def __init__(self):
        self.__socket = None
        self.__sel = None
        self.__player = None
    
    """
    __del__()
    deconstructs object.
    """    
    def __def__(self):
        self.__socket = None
        self.__sel = None
        self.__player = None
    
    """
    init()
    initializes the client.
    
    """    
    def Init(self,addr,port):
        try:
            
            self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            
            self.ModifyBufferSize(409600)
            
            self.__socket.connect((addr,port))
            
#            self.__socket.setblocking(False)
            
            self.__player = Player.BussinessClient(self.__socket,addr)
            self.__player.busShakeOnline()
            self.__player.Avtrans(True,False,False)
            
            self.IOmultiplexing()
        except OSError as e:
            print("socket error: %s ." %e)
            
    """
    IOmultiplexing()
    
    high-level and efficient I/O multiplexing
    """    
    def IOmultiplexing(self):
        self.__sel = selectors.DefaultSelector()
        self.__sel.register(self.__socket,selectors.EVENT_READ,self.Read)
        
        while True:
            events = self.__sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj,mask)
                
    """
    Read()
    
    
    """    
    def Read(self,conn,mask):
        data = conn.recv(HEADER_SIZE)
        
        if data: 
#            print("recv message: {},obj addr: {} ".format(data,id(data)))
            self.__player.Bussiness(data)
        else:
            print("client close.")
            self.__sel.unregister(conn)
            
    """
    ModifyBufferSize()
    
    
    """         
    def ModifyBufferSize(self,size):
        
        self.__socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            size)
        
        self.__socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_RCVBUF,
            size)
        
        bsize = self.__socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print("Buffer size [After] : %d" % bsize)
            
if __name__ == '__main__':
    client = TcpClient()
    client.Init('127.0.0.1',9916)
