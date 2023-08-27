import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class Overtake:
    def __init__(self, data):
        self.overtakingVehicleIdx = data[0]
        self.beingOvertakenVehicleIdx = data[1]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data,Overtake(packet)