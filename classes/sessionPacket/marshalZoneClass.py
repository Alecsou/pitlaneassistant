import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class MarshalZone:
    def __init__(self,data):
        self.zoneStart = data[0]
        self.zoneFlag = data[1]
    
    def __str__(self):
        return str(vars(self))

def decode(data):
    packet=[]
    tmp=0
    data,tmp=pt.getFloat(data)
    packet.append(tmp)
    data,tmp=pt.getSigned(data,8)
    packet.append(tmp)
    return data,MarshalZone(packet)
