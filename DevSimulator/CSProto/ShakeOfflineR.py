# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ShakeOfflineR(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsShakeOfflineR(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShakeOfflineR()
        x.Init(buf, n + offset)
        return x

    # ShakeOfflineR
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShakeOfflineR
    def Code(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShakeOfflineR
    def Msg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def ShakeOfflineRStart(builder): builder.StartObject(2)
def ShakeOfflineRAddCode(builder, code): builder.PrependInt32Slot(0, code, 0)
def ShakeOfflineRAddMsg(builder, msg): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(msg), 0)
def ShakeOfflineREnd(builder): return builder.EndObject()