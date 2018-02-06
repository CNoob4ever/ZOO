# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ControlAVTrans(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlAVTrans(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlAVTrans()
        x.Init(buf, n + offset)
        return x

    # ControlAVTrans
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlAVTrans
    def Audio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 1

    # ControlAVTrans
    def Video(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 1

    # ControlAVTrans
    def Subtitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def ControlAVTransStart(builder): builder.StartObject(3)
def ControlAVTransAddAudio(builder, audio): builder.PrependBoolSlot(0, audio, 1)
def ControlAVTransAddVideo(builder, video): builder.PrependBoolSlot(1, video, 1)
def ControlAVTransAddSubtitle(builder, subtitle): builder.PrependBoolSlot(2, subtitle, 0)
def ControlAVTransEnd(builder): return builder.EndObject()
