# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class OutputString(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsOutputString(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OutputString()
        x.Init(buf, n + offset)
        return x

    # OutputString
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OutputString
    def Msg(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def OutputStringStart(builder): builder.StartObject(1)
def OutputStringAddMsg(builder, msg): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(msg), 0)
def OutputStringEnd(builder): return builder.EndObject()