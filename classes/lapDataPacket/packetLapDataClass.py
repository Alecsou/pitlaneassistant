import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.lapDataPacket.lapDataClass as lapData;

class PacketLapData:
    def __init__(self,data):
        self.header = data[0] 
        self.lapData = data[1] 
        self.timeTrialPBCarIdx = data[2] 
        self.timeTrialRivalCarIdx = data[3]
    
    def __str__(self):
        return str(vars(self))

def decode(data,header):
    packet = [header]
    tmp = 0
    tab = []
    for _ in range(22):
        data,tmp = lapData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return PacketLapData(packet)