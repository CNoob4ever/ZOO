# -*- coding: utf-8 -*-
"""
purpose: Logger
author: Haluk
date: 1/25/2018
"""
import os
import logging.config

import yaml

class Logger:
    __instance = None
    """
    __new__()
    constructs Manager object.
    """
    def __new__(self):
        if not self.__instance:
            self.__instance = super(Logger,self).__new__(self)
            self.__logger = logging.getLogger()
        return self.__instance
    
    def __init__(self):
        self.setup_logging()
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__logger = None
    
    """
    Logself()
    self
    """
    def Logself(self):
        return self
    
    """
    __del__()
    setup logging
    """
    def setup_logging(
            self,
            default_path='./logcfg.yaml',
            default_level=logging.INFO,
            env_key='LOG_CFG'
        ):
        path = default_path
        value = os.getenv(env_key,None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path,'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            
    def debug(self,msg):
        self.__logger.debug(msg)
        
    def info(self,msg):
        self.__logger.info(msg)
        
    def warnning(self,msg):
        self.__logger.warning(msg)
        
    def error(self,msg):
        self.__logger.error(msg)
        
        

if __name__ == '__main__':
    pass;
