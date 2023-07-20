import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.carStatusPacket.carStatusDataClass as carStatusData
class PacketCarStatusData:
    def __init__(self, data):
        self.header = data[0]
        self.carStatusData = data[1]
    
    def __str__(self):
        return str(vars(self))

def decode(data,header):
    packet = [header]
    tmp = 0
    tab = []
    for _ in range(22):
        data,tmp = carStatusData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketCarStatusData(packet)