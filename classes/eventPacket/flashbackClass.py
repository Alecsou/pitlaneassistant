import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class Flashback:
    def __init__(self,data):
        self.flashbackFrameIdentifier = data[0]
        self.flashbackSessionTime = data[1]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    return data,Flashback(packet)