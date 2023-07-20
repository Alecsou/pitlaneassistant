import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.lobbyInfoPacket.lobbyInfoDataClass as lobbyInfoData;

class PacketLobbyInfoData:
    def __init__(self,data):
        self.header = data[0]
        self.numPlayers = data[1]
        self.lobbyPlayers = data[2]
    
    def __str__(self):
        return str(vars(self))

def decode(data,header):
    packet = [header]
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    tab = []
    for _ in range(22):
        data,tmp = lobbyInfoData.decode(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketLobbyInfoData(packet)
