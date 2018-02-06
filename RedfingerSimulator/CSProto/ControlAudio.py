# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ControlAudio(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlAudio(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlAudio()
        x.Init(buf, n + offset)
        return x

    # ControlAudio
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlAudio
    def Mode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # ControlAudio
    def Bitrate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 131072

def ControlAudioStart(builder): builder.StartObject(2)
def ControlAudioAddMode(builder, mode): builder.PrependUint8Slot(0, mode, 0)
def ControlAudioAddBitrate(builder, bitrate): builder.PrependUint32Slot(1, bitrate, 131072)
def ControlAudioEnd(builder): return builder.EndObject()
