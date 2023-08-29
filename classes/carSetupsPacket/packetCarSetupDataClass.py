import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.carSetupsPacket.carSetupDataClass as carSetupData;
import inspect;

class PacketCarSetupDataClass:
    def __init__(self,data):
        self.header = data[0]
        self.carSetups = data[1]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data,header):
    packet = [header]
    tmp = 0
    tab = []
    for _ in range(22):
        data,tmp = carSetupData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketCarSetupDataClass(packet)