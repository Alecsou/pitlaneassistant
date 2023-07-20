import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class FastestLap:
    def __init__(self,data):
        self.vehicleIdx = data[0]
        self.lapTime = data[1]
    
    def __str__(self):
        return str(vars(self))

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    return data,FastestLap(packet)