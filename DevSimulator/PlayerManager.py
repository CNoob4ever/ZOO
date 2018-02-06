# -*- coding: utf-8 -*-
"""
purpose: Client manager
author: Haluk
date: 1/25/2018
"""

class ClientManager:
    __instance = None
    """
    __new__()
    constructs Manager object.
    """
    def __new__(self):
        if not self.__instance:
            self.__instance = super(ClientManager,self).__new__(self)
            self.__PlayerDic = {}
        return self.__instance
    
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__PlayerDic.clear()
        
    def AddClient(self,conn,player):
        self.__PlayerDic[conn] = player
        
    def GetClient(self,conn):
        return self.__PlayerDic.get(conn)
        
    def RemoveClient(self,conn):
        self.__PlayerDic.pop(conn)
        
    def ClearAll(self):
        self.__PlayerDic.clear()
        
    def Dic(self):
        return self.__PlayerDic
        
if __name__ == '__main__':
    pass;