# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class OutputScreen(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsOutputScreen(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = OutputScreen()
        x.Init(buf, n + offset)
        return x

    # OutputScreen
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OutputScreen
    def Rotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # OutputScreen
    def Width(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 1280

    # OutputScreen
    def Height(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 720

    # OutputScreen
    def Fps(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 60

def OutputScreenStart(builder): builder.StartObject(4)
def OutputScreenAddRotation(builder, rotation): builder.PrependInt8Slot(0, rotation, 0)
def OutputScreenAddWidth(builder, width): builder.PrependUint16Slot(1, width, 1280)
def OutputScreenAddHeight(builder, height): builder.PrependUint16Slot(2, height, 720)
def OutputScreenAddFps(builder, fps): builder.PrependUint16Slot(3, fps, 60)
def OutputScreenEnd(builder): return builder.EndObject()
