# -*- coding: utf-8 -*-
"""
purpose: Server
author: Haluk
date: 1/25/2018
"""

import socket
import selectors

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
        
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__port = 9916
        self.__socket = None
        self.__sel = None
        
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
        
            self.__socket.setblocking(False);
            
            self.IOmultiplexing()
                
        except OSError as e: 
            print("socket error: %s ." %e)
        except KeyboardInterrupt as ki:
            print("keybordInterrupt %s ." %ki)
            
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
        print('accpted ', conn,' from ',addr)
        conn.setblocking(False)
        self.__sel.register(conn,selectors.EVENT_READ,self.Read)
        
    """
    Read()
    
    
    """    
    def Read(self,conn,mask):
        data = conn.recv(10)
        if data:
            print("recv message")
        else:
            print("client close.")
            self.__sel.unregister(conn)
        
if __name__ == '__main__':
    server = TcpServer()
    server.Init(9916)
