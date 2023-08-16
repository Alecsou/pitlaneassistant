import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class MarshalZone:
    def __init__(self,data):
        self.zoneStart = data[0]
        self.zoneFlag = data[1]
    
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

def decode(data):
    packet=[]
    tmp=0
    data,tmp=pt.getFloat(data)
    packet.append(tmp)
    data,tmp=pt.getSigned(data,8)
    packet.append(tmp)
    return data,MarshalZone(packet)
