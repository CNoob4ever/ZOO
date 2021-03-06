# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class InputGyro(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInputGyro(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InputGyro()
        x.Init(buf, n + offset)
        return x

    # InputGyro
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InputGyro
    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # InputGyro
    def Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # InputGyro
    def Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def InputGyroStart(builder): builder.StartObject(3)
def InputGyroAddX(builder, x): builder.PrependFloat32Slot(0, x, 0.0)
def InputGyroAddY(builder, y): builder.PrependFloat32Slot(1, y, 0.0)
def InputGyroAddZ(builder, z): builder.PrependFloat32Slot(2, z, 0.0)
def InputGyroEnd(builder): return builder.EndObject()
