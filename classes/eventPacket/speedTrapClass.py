import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class SpeedTrap:
    def __init__(self, data):
        self.vehicleIdx = data[0]
        self.speed = data[1]
        self.isOverallFastestInSession = data[2]
        self.isDriverFastestInSession = data[3]
        self.fastestSpeedInSession = data[4]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    return data,SpeedTrap(packet)