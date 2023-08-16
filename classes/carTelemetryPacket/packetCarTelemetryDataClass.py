import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.carTelemetryPacket.carTelemetryDataClass as carTelemetryData
import inspect;

class PacketCarTelemetryData:
    def __init__(self, data):
        self.header = data[0]
        self.carTelemetrydata = data[1]
        self.mfdPanelIndex = data[2]
        self.mfdPanelIndexSecondaryPlayer = data[3]
        self.suggestedGear = data[4]
    
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
        data,tmp = carTelemetryData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getSigned(data,8)
    packet.append(tmp)
    return PacketCarTelemetryData(packet)