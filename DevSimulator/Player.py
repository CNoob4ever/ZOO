# -*- coding: utf-8 -*-
"""
purpose: Bussiness object
author: Haluk
date: 1/25/2018
"""
import time
import struct
import datetime
import threading
import flatbuffers

from Logger import Logger

from CSProto import ShakeOnline
from CSProto import ShakeOnlineR
from CSProto import ControlAVTrans

import ProtocalHeader

class BussinessClient:
    """
    __init__()
    constructs tcp object.
    """
    def __init__(self,conn,addr):
        self.__socket = conn
        self.__addr = addr
        self.__Parse = ProtocalHeader.ProtocalHeader()
        self.__lock = threading.Lock()
        self.__vFps = 30
        self.__aFps = 1
        self.__videoRuning = False
        self.__audioRuning = False
        self.__log = Logger()
        
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__socket = None
        self.__addr = None
        self.__Parse = None
        self.__lock = None
        self.__vFps = 30
        self.__aFps = 1
        self.__videoRuning = False
        self.__audioRuning = False
        self.__log = None
        
    """
    Bussiness()
    deconstructs object.
    """
    def Bussiness(self,data):
#        print("processes data: {}, obj addr: {}" .format(data,id(data)))
        types,subtypes,length = self.__Parse.Parse(data)
#        print("types: {},subtypes: {},length: {} ".format(types,subtypes,length))
        
        priType = ProtocalHeader.MSG_TYPE(types)
        body = self.__socket.recv(length)
#        if sys.getsizeof(body) !=  length:
#            print("body length abnormal.")
#            return
        
        if priType is ProtocalHeader.MSG_TYPE.MSG_SHAKE:
            secType = ProtocalHeader.MSG_SHAKE_TYPE(subtypes)
            if secType is ProtocalHeader.MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE:
                self.ShakeOnline(body)
            elif secType is ProtocalHeader.MSG_SHAKE_TYPE.MSG_SHAKE_OFFLINE:
                pass;
            else:
                self.__log.warnning("Don't support subtype: {}".format(secType))
        elif priType is ProtocalHeader.MSG_TYPE.MSG_CONTROL:
            secType = ProtocalHeader.MSG_CONTROL_TYPE(subtypes)
            if secType is ProtocalHeader.MSG_CONTROL_TYPE.MSG_CONTROL_AVTRANS:
                self.Avtrans(body)
            else:
                self.__log.warnning("Don't support subtype: {}".format(secType))
        elif priType is ProtocalHeader.MSG_TYPE.MSG_INPUT:
            secType = ProtocalHeader.MSG_INPUT_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_OUTPUT:
            secType = ProtocalHeader.MSG_OUTPUT_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_AV:
            secType = ProtocalHeader.MSG_AV_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_AUTH:
            secType = ProtocalHeader.MSG_AUTH_TYPE(subtypes)
            pass;
        else:
            self.__log.error("primitive types Error : {}".format(priType))
        
    """
    Send()
    
    """
    def Send(self,types,subtypes,length,data):
        try:
#            print("send types: {},subtypes: {},length: {}".format(types,subtypes,length))
            self.__lock.acquire()
            msgFormat = '@2BI' + str(length) +'s'
            package = struct.pack(msgFormat,types,subtypes,length,data)
            self.__socket.send(package)
        except OSError as e:
            self.__log.error("send error: {}".format(e))
        except struct.error as e:
            self.__log.error("send error: {}".format(e))
        finally:
            self.__lock.release()
            
    def ShakeOnline(self,data):
        shakeOnline = ShakeOnline.ShakeOnline.GetRootAsShakeOnline(data,0)
        dataId = shakeOnline.Id()
        if dataId == "":
            self.__log.error("shake online error.")
            self.__socket.close()
            
        builder = flatbuffers.Builder(1024)
        msg = builder.CreateString("ok")
        Id = builder.CreateString(dataId)
        ShakeOnlineR.ShakeOnlineRStart(builder)
        ShakeOnlineR.ShakeOnlineRAddCode(builder,0)
        ShakeOnlineR.ShakeOnlineRAddMsg(builder,msg)
        ShakeOnlineR.ShakeOnlineRAddId(builder,Id)
        info = ShakeOnlineR.ShakeOnlineREnd(builder)
        builder.Finish(info)
        
        output = builder.Output()
        
        self.Send(ProtocalHeader.MSG_TYPE.MSG_SHAKE.value,
                  ProtocalHeader.MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE_R.value,
                  len(output),
                  output)
        
        
    def ShakeOffline(self):
        pass;
        
    def Avtrans(self,data):
        avTrans = ControlAVTrans.ControlAVTrans.GetRootAsControlAVTrans(data,0)
        self.__audioRuning = avTrans.Audio()
        self.__videoRuning = avTrans.Video()
        dataSubtitle = avTrans.Subtitle()
        
#        print("avtrans audio: {}, Video: {}, Subtitle: {}".format(self.__audioRuning, self.__videoRuning,dataSubtitle))
        
        if self.__videoRuning:
            vThr = threading.Thread(target = self.VideoThr)
            vThr.start()
        if self.__audioRuning:
            aThr = threading.Thread(target = self.AudioThr)
            aThr.start()
        
        
    def VideoThr(self):
        body = bytes(b'\0')*102400
        length = len(body)
        while self.__videoRuning:
            oldTime = datetime.datetime.now()
            
            self.Send(ProtocalHeader.MSG_TYPE.MSG_AV.value,
                  ProtocalHeader.MSG_AV_TYPE.MSG_AV_VIDEO.value,
                  length,
                  body)
            
            processTime = 1000/self.__vFps
            
            nowTime = datetime.datetime.now()
            elapsed = (nowTime - oldTime).microseconds/1000
            if elapsed < processTime:
                time.sleep((processTime-elapsed)/1000)
#                print("video sleep: ",processTime-elapsed)
        
    def AudioThr(self):
        body = bytes(b'\0')*100
        length = len(body)
        while self.__audioRuning:
            oldTime = datetime.datetime.now()
            
            self.Send(ProtocalHeader.MSG_TYPE.MSG_AV.value,
                  ProtocalHeader.MSG_AV_TYPE.MSG_AV_AUDIO.value,
                  length,
                  body)
            
            processTime = 1000/self.__aFps
            
            nowTime = datetime.datetime.now()
            elapsed = (nowTime - oldTime).microseconds/1000
            if elapsed < processTime:
                time.sleep((processTime-elapsed)/1000)
#                print("video sleep: ",processTime-elapsed)
        
if __name__ == '__main__':
    pass;
    
    
    