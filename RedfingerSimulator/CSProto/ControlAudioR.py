# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ControlAudioR(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlAudioR(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlAudioR()
        x.Init(buf, n + offset)
        return x

    # ControlAudioR
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlAudioR
    def Code(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ControlAudioR
    def Msg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # ControlAudioR
    def Profile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # ControlAudioR
    def Channel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 2

    # ControlAudioR
    def Smprate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 44100

    # ControlAudioR
    def Bitrate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 131072

def ControlAudioRStart(builder): builder.StartObject(6)
def ControlAudioRAddCode(builder, code): builder.PrependInt32Slot(0, code, 0)
def ControlAudioRAddMsg(builder, msg): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(msg), 0)
def ControlAudioRAddProfile(builder, profile): builder.PrependUint8Slot(2, profile, 0)
def ControlAudioRAddChannel(builder, channel): builder.PrependUint8Slot(3, channel, 2)
def ControlAudioRAddSmprate(builder, smprate): builder.PrependUint32Slot(4, smprate, 44100)
def ControlAudioRAddBitrate(builder, bitrate): builder.PrependUint32Slot(5, bitrate, 131072)
def ControlAudioREnd(builder): return builder.EndObject()
