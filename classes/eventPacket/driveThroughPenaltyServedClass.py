import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class DriveThroughPenaltyServed:
    def __init__(self, data):
        self.vehicleIdx = data[0]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,DriveThroughPenaltyServed(packet)