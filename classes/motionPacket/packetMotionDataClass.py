import classes.motionPacket.carMotionDataClass as carMotionDataClass;
import inspect;

class PacketMotionData:
    def __init__(self,data):
        self.header = data[0]
        self.carMotionData = data[1]
    
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
        data,tmp = carMotionDataClass.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketMotionData(packet)