import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.carDamagePacket.carDamageDataClass as carDamageData;

class PacketCarDamageData:
    def __init__(self,data):
        self.header= data[0]
        self.carDamageData = data[1]
    
    def __str__(self):
        return str(vars(self))

def decode(data,header):
    packet = [header]
    tmp = 0
    tab = []
    for _ in range(22):
        data,tmp = carDamageData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketCarDamageData(packet)