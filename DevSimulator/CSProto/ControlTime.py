# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ControlTime(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlTime(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlTime()
        x.Init(buf, n + offset)
        return x

    # ControlTime
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlTime
    def Time(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ControlTimeStart(builder): builder.StartObject(1)
def ControlTimeAddTime(builder, time): builder.PrependInt32Slot(0, time, 0)
def ControlTimeEnd(builder): return builder.EndObject()
