import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.finalClassificationPacket.finalClassificationDataClass as finalClassificationData;
import inspect;

class PacketFinalClassificationData:
    def __init__(self,data):
        self.header = data[0]
        self.numCars = data[1]
        self.classificationData = data[2]
    
    def __str__(self):
        s="{"
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    if type(i[1]) is list:
                        ss = "["
                        for _ in i[1]:
                            ss+=str(_)+", "
                        ss+="]"
                    else:
                        ss=str(i[1])
                    s+=str(i[0])+ " : " +ss+", "
        return s+"}"
    
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