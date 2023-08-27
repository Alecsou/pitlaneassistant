import classes.motionPacket.carMotionDataClass as carMotionDataClass;
import inspect;

import parseTypes as pt;

class PacketMotionData:
    def __init__(self,data):
        self.header = data[0]
        self.carMotionData = data[1]
    
    def __str__(self):
        return pt.getStr(self)
                

def decode(data,header):
    packet = [header]
    tmp = 0
    tab = []
    for _ in range(22):
        data,tmp = carMotionDataClass.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketMotionData(packet)