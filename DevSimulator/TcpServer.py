# -*- coding: utf-8 -*-
"""
purpose: Server
author: Haluk
date: 1/25/2018
"""

import socket
import selectors
import struct 
import Player
import PlayerManager 

from Logger import Logger

HEADER_SIZE = struct.calcsize('@2BI')

class TcpServer:
    """
    __init__()
    constructs tcp object.
    
    m_port:     listening port
    m_socket:   socket
    """
    def __init__(self):
        self.__port = 9916
        self.__socket = None
        self.__sel = None
        self.__PlayerManager = PlayerManager.ClientManager()
        self.__log = Logger()
        
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__port = 9916
        self.__socket = None
        self.__sel = None
        self.__PlayerManager = None
        self.__log = None
        
    """
    init()
    initializes the server.
    
    """
    def Init(self,port):
        try:
            self.__port = port
        
            self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
            self.__socket.bind(('localhost',port))
        
            self.__socket.listen(3)
            
            self.__log.info("listening on {}".format(port))
        
            self.__socket.setblocking(False)
            
            self.ModifyBufferSize(409600)
            
            self.IOmultiplexing()
                
        except OSError as e:
            self.__log.error("socket error: {}.".format(e))
            
    """
    IOmultiplexing()
    
    high-level and efficient I/O multiplexing
    """    
    def IOmultiplexing(self):
        self.__sel = selectors.DefaultSelector()
        self.__sel.register(self.__socket,selectors.EVENT_READ,self.Accept)
        
        while True:
            events = self.__sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj,mask)
                
    """
    Accept()
    
    
    """            
    def Accept(self,soke,mask):
        conn, addr = self.__socket.accept()
        self.__log.info("accpted  {} from {}".format(conn,addr))
        conn.setblocking(False)
        self.__sel.register(conn,selectors.EVENT_READ,self.Read)
        self.__PlayerManager.AddClient(conn,Player.BussinessClient(conn,addr))
        
    """
    Read()
    
    
    """    
    def Read(self,conn,mask):
        data = conn.recv(HEADER_SIZE)
        
        if data:
            self.__log.debug("recv message: {} ".format(data))
            self.__PlayerManager.GetClient(conn).Bussiness(data)
            
            
        else:
            self.__log.info("client close.")
            self.__sel.unregister(conn)
            self.__PlayerManager.RemoveClient(conn)
    
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
        
#        bsize = self.__socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
#        print("Buffer size [After] : %d" % bsize)
        
if __name__ == '__main__':
    pass;
