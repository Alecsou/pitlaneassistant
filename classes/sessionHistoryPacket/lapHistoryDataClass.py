import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class LapHistoryData:
    def __init__(self,data):
        self.lapTimeInMS = data[0]
        self.sector1TimeInMS = data[1] 
        self.sector1TimeMinutes = data[2]
        self.sector2TimeInMS = data[3] 
        self.sector1TimeMinutes = data[4] 
        self.sector3TimeInMS = data[5]
        self.sector3TimeMinutes = data[6]
        self.lapValidBitFlags = data[7] 
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data, LapHistoryData(packet)
