import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class ParticipantData:
    def __init__(self,data):
        self.aiControlled = data[0]
        self.driverId = data[1]
        self.networkId = data[2]
        self.teamId = data[3]
        self.myTeam = data[4]
        self.raceNumber = data[5]
        self.nationality = data[6]
        self.name = data[7]
        self.yourTelemetry = data[8]
        self.showOnlineNames = data[9]
        self.platform = data[10]
    
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
    packet = []
    tmp = 0
    for _ in range(7):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    s = ""
    for _ in range(48):
        data,tmp = pt.getChar(data)
        s+=tmp
    packet.append(s)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data,ParticipantData(packet)
