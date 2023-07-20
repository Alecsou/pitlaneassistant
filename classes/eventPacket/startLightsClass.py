import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
class StartLights:
    def __init__(self, data):
        self.numLights = data[0]
    
    def __str__(self):
        return str(vars(self))
    
def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,StartLights(packet)