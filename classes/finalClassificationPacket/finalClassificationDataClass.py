import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class FinalClassificationData:
    def __init__(self,data):
        self.position = data[0]
        self.numLaps = data[1] 
        self.gridPosition = data[2] 
        self.points = data[3] 
        self.numPitStops = data[4] 
        self.resultStatus = data[5] 
        self.bestLapTimeInMS = data[6]
        self.totalRaceTime = data[7] 
        self.penaltiesTime = data[8]
        self.numPenalties = data[9] 
        self.numTyreStints = data[10] 
        self.tyreStintsActual = data[11] 
        self.tyreStintsVisual = data[12] 
        self.tyreStintsEndLaps = data[13]
    
    def __str__(self):
        return str(vars(self))

def decode(data):
    packet = []
    tmp = 0
    for _ in range(6):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    data,tmp = pt.getDouble(data)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(3):
        tab = []
        for __ in range(8):
            data,tmp = pt.getUnsigned(data,8)
            tab.append(tmp)
        packet.append(tab)
    return data,FinalClassificationData(packet)
