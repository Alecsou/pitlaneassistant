import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.finalClassificationPacket.finalClassificationDataClass as finalClassificationData;

class PacketFinalClassificationData:
    def __init__(self,data):
        self.header = data[0]
        self.numCars = data[1]
        self.classificationData = data[2]
    
    def __str__(self):
        return str(vars(self))
    
def decode(data,header):
    packet = [header]
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    tab = []
    for _ in range(22):
        data,tmp = finalClassificationData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketFinalClassificationData(packet)