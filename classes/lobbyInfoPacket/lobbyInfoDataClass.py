import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class LobbyInfoData:
    def __init__(self,data):
        self.aiControlled = data[0]
        self.teamId = data[1]
        self.nationality = data[2]
        self.platform = data[3]
        self.name = data[4]
        self.carNumber = data[5]
        self.readyStatus = data[6]

    def __str__(self):
        return str(vars(self))

def decode(data):
    packet = []
    tmp = 0
    for _ in range(4):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    str = ""
    for _ in range(48):
        data,tmp = pt.getChar(data)
        str+=tmp
    packet.append(str)
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data,LobbyInfoData(packet)