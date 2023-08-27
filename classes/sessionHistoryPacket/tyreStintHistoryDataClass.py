import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class TyreStintHistoryData:
    def __init__(self,data):
        self.endLap = data[0]
        self.tyreActualCompound = data[1]
        self.tyreVisualCompound = data[2]

    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data, TyreStintHistoryData(packet)