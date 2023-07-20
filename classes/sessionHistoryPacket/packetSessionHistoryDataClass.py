import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.sessionHistoryPacket.lapHistoryDataClass as lapHistoryData;
import classes.sessionHistoryPacket.tyreStintHistoryDataClass as tyreStintHistoryData;

class PacketSessionHistoryData:
    def __init__(self,data):
        self.header = data[0] 
        self.carIdx = data[1] 
        self.numLaps = data[2]
        self.numTyreStints = data[3] 
        self.bestLapTimeLapNum = data[4] 
        self.bestSector1LapNum = data[5]
        self.bestSector2LapNum = data[6] 
        self.bestSector3LapNum = data[7]
        self.lapHistoryData = data[8] 
        self.tyreStintsHistoryData = data[9]
    
    def __str__(self):
        return str(vars(self))

def decode(data,header):
    packet = [header]
    tmp = 0
    for _ in range(7):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    tab = []
    for _ in range(100):
        data,tmp = lapHistoryData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    tab = []
    for _ in range(8):
        data,tmp = tyreStintHistoryData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketSessionHistoryData(packet)

