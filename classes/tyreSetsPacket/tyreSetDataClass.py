import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class TyreSetData:
    def __init__(self,data):
        self.actualTyreCompound = data[0] 
        self.visualTyreCompound = data[1] 
        self.wear = data[2]
        self.available = data[3] 
        self.recommendedSession = data[4]
        self.lifeSpan = data[5] 
        self.usableLife = data[6]
        self.lapDeltaTime = data[7] 
        self.fitted = data[8] 
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    for _ in range(7):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getSigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data, TyreSetData(packet)