# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class ShakeKickR(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsShakeKickR(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShakeKickR()
        x.Init(buf, n + offset)
        return x

    # ShakeKickR
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ShakeKickR
    def Code(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ShakeKickR
    def Msg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def ShakeKickRStart(builder): builder.StartObject(2)
def ShakeKickRAddCode(builder, code): builder.PrependInt32Slot(0, code, 0)
def ShakeKickRAddMsg(builder, msg): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(msg), 0)
def ShakeKickREnd(builder): return builder.EndObject()
