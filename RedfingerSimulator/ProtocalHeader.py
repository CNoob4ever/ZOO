# -*- coding: utf-8 -*-
"""
purpose: Bussiness object
author: Haluk
date: 1/25/2018
"""

import struct 
from enum import Enum

"""
typedef struct _csproto_header_t
{
    unint8_t  type;
    unint8_t  subtype;
    unint32_t len;
}
"""

class ProtocalHeader:
    """
    __init__()
    constructs protocal object.
    """
    def __init__(self):
        self.__proto_header_t = struct.Struct('@2BI')
    
    """
    __del__()
    deconstructs object.
    """
    def __def__(self):
        self.__proto_header_t = None
        
    def Parse(self,data):
        try:
            return self.__proto_header_t.unpack_from(data)
        except struct.error as e:
            print("struct error: ", e)
            
    def Serialize(self,types,subtypes,lengths):
        try:
            return self.__proto_header_t.pack(types,subtypes,lengths)
        except struct.error as e:
            print("pack error: ", e)
            
class MSG_TYPE(Enum):
    MSG_SHAKE                   = 0     # 握手协议
    MSG_CONTROL                 = 1     # 控制协议
    MSG_INPUT                   = 2 	 # 操控/输入协议
    MSG_OUTPUT                  = 3 	 # 输出协议
    MSG_AV                      = 4     # 音视频协议
    MSG_AUTH                    = 5     # 权限协议，专用于设备和流媒体服务器
    
class MSG_SHAKE_TYPE(Enum):
    MSG_SHAKE_ONLINE            = 0 	# 上线请求
    MSG_SHAKE_ONLINE_R          = 1 	# 上线应答
    MSG_SHAKE_OFFLINE           = 2 	# 下线请求
    MSG_SHAKE_OFFLINE_R         = 3 	# 下线应答
    MSG_SHAKE_KICK              = 4 	# 强制踢出请求
    
class MSG_CONTROL_TYPE(Enum):
    MSG_CONTROL_MTU					= 0     # MTU测试请求
    MSG_CONTROL_MTU_R				= 1     # MTU测试应答
    MSG_CONTROL_DELAY				= 2     # 延迟测试请求
    MSG_CONTROL_DELAY_R				= 3     # 延迟测试应答
    MSG_CONTROL_APP					= 4     # 应用请求
    MSG_CONTROL_APP_R				= 5     # 应用应答 
    MSG_CONTROL_AVFMT				= 6 	  # 音视频格式请求，数据结构内的值只是个要求，真正的值由服务器决定
    MSG_CONTROL_AVFMT_R				= 7 	  # 音视频格式应答
    MSG_CONTROL_AVTRANS				= 8 	  # 音视频传输控制请求（是否传输音频、视频）
    MSG_CONTROL_AVTRANS_R			= 9     # 音视频传输控制应答
    MSG_CONTROL_IFRAME				= 10 	  # 视频关键帧请求
    MSG_CONTROL_AUDIO				= 11    # 音频参数调整请求
    MSG_CONTROL_AUDIO_R				= 12	  # 音频参数应答
    MSG_CONTROL_VIDEO				= 13 	  # 视频参数调整请求
    MSG_CONTROL_VIDEO_R				= 14	  # 视频参数应答
    MSG_CONTROL_TIME				   = 15	  # 控制倒计时
    MSG_CONTROL_SCREEN				= 16    # 屏幕分辨率比例设置
    MSG_CONTROL_KILL_APP			= 17    #杀死app
    MSG_CONTROL_KILL_APP_R			= 18	  #杀死app应答
    MSG_CONTROL_RESOLUTIONLEVEL	= 19	  #分辨率级别
    
class MSG_INPUT_TYPE(Enum):
    # 通用
    MSG_INPUT_STRING            = 0	   # 字符串
    MSG_INPUT_GAMECONTROLLER    = 1 	# 游戏控制器

    # PC
    MSG_INPUT_KEYBOARD          = 100 	 # 键盘
    MSG_INPUT_MOUSE_KEY         = 101 	 # 鼠标按键
    MSG_INPUT_MOUSE_WHEEL       = 102 	 # 鼠标滚轮
    MSG_INPUT_MOUSE_MOVE        = 103 	 # 鼠标移动
    MSG_INPUT_CURSOR            = 104   # 光标，你可以认为就是鼠标箭头

    # 手机
    MSG_INPUT_TOUCH             = 200 	 # 触摸
    MSG_INPUT_LOCATION          = 201   # 位置数据
    MSG_INPUT_ACCELEROMETER     = 202   # 加速度
    MSG_INPUT_ALTIMETER         = 203   # 高度计
    MSG_INPUT_GYRO              = 204   # 陀螺仪
    MSG_INPUT_MAGNETOMETER      = 205   # 磁力计
    MSG_INPUT_PEDOMETER         = 206   # 计步器
    MSG_INPUT_PROXIMITY         = 207   # 距离传感器
    MSG_INPUT_AMBIENTLIGHT      = 208   # 环境光传感器
    MSG_INPUT_TEMPERATURE       = 209   # 温度传感器
    MSG_INPUT_MOISTURE          = 210   # 湿度传感器
    
class MSG_OUTPUT_TYPE(Enum):
    MSG_OUTPUT_STRING           = 0     # 字符串
    MSG_OUTPUT_SCREEN           = 1     # 屏幕相关，分辨率，刷新率，旋转
    MSG_OUTPUT_VIBRATION        = 2 	 # 震动
    MSG_OUTPUT_CURSOR           = 3 	 # 光标位置及可见性
    
class MSG_AV_TYPE(Enum):
    MSG_AV_AUDIO                = 0    # 音频
    MSG_AV_VIDEO                = 1    # 视频
    MSG_AV_SUBTITLE             = 2    # 字幕
    MSG_AV_CLIENT_AUDIO         = 3    # 客户端音频
    MSG_AV_CLIENT_VIDEO         = 4    # 客户端视频
    MSG_AV_CLIENT_SUBTITLE      = 5    # 客户端字幕
    
class MSG_AUTH_TYPE(Enum):
    MSG_AUTH_LIST               = 0    # 权限列表
    
class AUDIO_FMT_TYPE(Enum):
    AUDIO_FMT_AAC           = 0
    
  
if __name__ == '__main__':
#    tempdata = struct.pack('@2BI',MSG_TYPE.MSG_SHAKE.value,MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE.value,100)
    P = ProtocalHeader()
    tempdata = P.Serialize(MSG_TYPE.MSG_SHAKE.value,MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE.value,100)
#    tempdata = None
#    P.Serialize(tempdata,MSG_TYPE.MSG_SHAKE.value,MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE.value,100)
    types,subtypes,length = P.Parse(tempdata)
    print("types: {},subtypes: {},length: {} ".format(types,subtypes,length))
    
    
    msgtype = MSG_TYPE(types)
    if msgtype is MSG_TYPE.MSG_SHAKE:
        print("MSG_TYPE.MSG_SHAKE")
    elif msgtype is MSG_TYPE.MSG_CONTROL:
        print("MSG_TYPE.MSG_CONTROL")
    else:
        print("end")
    
    length = 10
    pformat = '@2BI' + str(length) +'s'
    testdata = struct.pack(pformat,MSG_TYPE.MSG_SHAKE.value,MSG_SHAKE_TYPE.MSG_SHAKE_ONLINE.value,100,b'1354fsdfef')
    types1,subtypes1,length1,string = struct.unpack(pformat,testdata)
    print("types: {},subtypes: {},length: {},string: {} ".format(types1,subtypes1,length1,string))
    