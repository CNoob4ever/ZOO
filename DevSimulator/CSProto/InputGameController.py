# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CSProto

import flatbuffers

class InputGameController(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInputGameController(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InputGameController()
        x.Init(buf, n + offset)
        return x

    # InputGameController
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InputGameController
    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Buttons(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Lt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Rt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Lx(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Ly(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Rx(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # InputGameController
    def Ry(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def InputGameControllerStart(builder): builder.StartObject(8)
def InputGameControllerAddIndex(builder, index): builder.PrependUint8Slot(0, index, 0)
def InputGameControllerAddButtons(builder, buttons): builder.PrependUint16Slot(1, buttons, 0)
def InputGameControllerAddLt(builder, lt): builder.PrependUint8Slot(2, lt, 0)
def InputGameControllerAddRt(builder, rt): builder.PrependUint8Slot(3, rt, 0)
def InputGameControllerAddLx(builder, lx): builder.PrependInt16Slot(4, lx, 0)
def InputGameControllerAddLy(builder, ly): builder.PrependInt16Slot(5, ly, 0)
def InputGameControllerAddRx(builder, rx): builder.PrependInt16Slot(6, rx, 0)
def InputGameControllerAddRy(builder, ry): builder.PrependInt16Slot(7, ry, 0)
def InputGameControllerEnd(builder): return builder.EndObject()