import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.carDamagePacket.carDamageDataClass as carDamageData;
import inspect;

class PacketCarDamageData:
    def __init__(self,data):
        self.header= data[0]
        self.carDamageData = data[1]
    
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
    tab = []
    for _ in range(22):
        data,tmp = carDamageData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketCarDamageData(packet)