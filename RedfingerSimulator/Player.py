# -*- coding: utf-8 -*-
"""
purpose: Client
author: Haluk
date: 1/25/2018
"""
import sys
import struct
import threading
import flatbuffers

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
    
    """
    __del__()
    deconstructs object.
    """
    def __del__(self):
        self.__socket = None
        self.__addr = None
        self.__Parse = None
        self.__lock = None
    
    """
    Bussiness()
    deconstructs object.
    """    
    def Bussiness(self,data):
#        print("processes data: {}, obj addr: {}" .format(data,id(data)))
        types,subtypes,length = self.__Parse.Parse(data)
        if length > 0:
            print("types: {},subtypes: {},length: {} ".format(types,subtypes,length))
        
        priType = ProtocalHeader.MSG_TYPE(types)
        body = self.__socket.recv(length)
#        if sys.getsizeof(body) !=  length:
#            print("body length({}) abnormal[types: {},subtypes: {},length: {}]".format(len(body),types,subtypes,length))
#            return
        
        if priType is ProtocalHeader.MSG_TYPE.MSG_SHAKE:
            secType = ProtocalHeader.MSG_SHAKE_TYPE(subtypes)
            if secType is ProtocalHeader.MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE_R:
                self.busShakeOnlineR(body)
            else:
                pass;
#                print("Don't support subtype: ",secType)
        elif priType is ProtocalHeader.MSG_TYPE.MSG_CONTROL:
            secType = ProtocalHeader.MSG_CONTROL_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_INPUT:
            secType = ProtocalHeader.MSG_INPUT_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_OUTPUT:
            secType = ProtocalHeader.MSG_OUTPUT_TYPE(subtypes)
            pass;
        elif priType is ProtocalHeader.MSG_TYPE.MSG_AV:
            secType = ProtocalHeader.MSG_AV_TYPE(subtypes)
            if secType is ProtocalHeader.MSG_AV_TYPE.MSG_AV_VIDEO:
                self.Video()
            elif secType is ProtocalHeader.MSG_AV_TYPE.MSG_AV_AUDIO:
                self.Audio()
            else:
                pass;
#                print("Don't support subtype: ",secType)
        elif priType is ProtocalHeader.MSG_TYPE.MSG_AUTH:
            secType = ProtocalHeader.MSG_AUTH_TYPE(subtypes)
            pass;
        else:
            print("primitive types Error : ",priType);
    
    """
    Send()
    
    """    
    def Send(self,types,subtypes,length,data):
        try:
            self.__lock.acquire()
            msgFormat = '@2BI' + str(length) +'s'
            package = struct.pack(msgFormat,types,subtypes,length,data)
            self.__socket.send(package)
        except OSError as e:
            print("send error: ", e)
        except struct.error as e:
            print("pack error: ", e)
        finally:
            self.__lock.release()
            
    def busShakeOnline(self):
        builder = flatbuffers.Builder(1024)
        
        Id = builder.CreateString("1452358")
        token = builder.CreateString("askhdwihydgfijfrifjewojfuie")
        server = builder.CreateString("IUEFUBWEJ")
        app = builder.CreateString("qwedasd")
        
        ShakeOnline.ShakeOnlineStart(builder)
        ShakeOnline.ShakeOnlineAddId(builder,Id)
        ShakeOnline.ShakeOnlineAddToken(builder,token)
        ShakeOnline.ShakeOnlineAddServer(builder,server)
        ShakeOnline.ShakeOnlineAddApp(builder,app)
        ShakeOnline.ShakeOnlineAddType(builder,25)
        info = ShakeOnline.ShakeOnlineEnd(builder)
        builder.Finish(info)
        body = builder.Output()
        
        self.Send(ProtocalHeader.MSG_TYPE.MSG_SHAKE.value,
                  ProtocalHeader.MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE.value,
                  len(body),
                  body)
        
    def busShakeOnlineR(self,data):
        shakeOnlineR = ShakeOnlineR.ShakeOnlineR.GetRootAsShakeOnlineR(data,0)
        
        code = shakeOnlineR.Code()
        msg = shakeOnlineR.Msg()
        Id = shakeOnlineR.Id()
        
        print("shakeOnlineR code: {}, msg: {}, id: {}.".format(code,msg,Id))
        
    def Avtrans(self,video,audio,subtitle):
        builder = flatbuffers.Builder(1024)
        
        ControlAVTrans.ControlAVTransStart(builder)
        ControlAVTrans.ControlAVTransAddVideo(builder,video)
        ControlAVTrans.ControlAVTransAddAudio(builder,audio)
        ControlAVTrans.ControlAVTransAddSubtitle(builder,subtitle)
        info = ControlAVTrans.ControlAVTransEnd(builder)
        builder.Finish(info)
        body = builder.Output()
        
        self.Send(ProtocalHeader.MSG_TYPE.MSG_CONTROL.value,
                  ProtocalHeader.MSG_CONTROL_TYPE.MSG_CONTROL_AVTRANS.value,
                  len(body),
                  body)
        
    def Video(self):
        print("video")
        
    def Audio(self):
        print("audio")
        
if __name__ == '__main__':
    pass;