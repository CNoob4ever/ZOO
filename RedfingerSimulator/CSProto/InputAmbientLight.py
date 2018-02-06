# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class InputAmbientLight(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInputAmbientLight(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InputAmbientLight()
        x.Init(buf, n + offset)
        return x

    # InputAmbientLight
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InputAmbientLight
    def Reserved(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def InputAmbientLightStart(builder): builder.StartObject(1)
def InputAmbientLightAddReserved(builder, reserved): builder.PrependFloat32Slot(0, reserved, 0.0)
def InputAmbientLightEnd(builder): return builder.EndObject()
