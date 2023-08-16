import inspect;

class Header:
    def __init__(self,data):
        self.packetFormat = data[0]
        self.gameYear = data[1]
        self.gameMajorVersion = data[2]
        self.gameMinorVersion = data[3]
        self.packetVersion = data[4]
        self.packetId = data[5]
        self.sessionUID = data[6]
        self.sessionTime = data[7]
        self.frameIdentifier = data[8]
        self.overallFrameIdentifier = data[9]
        self.playerCarIndex = data[10]
        self.secondaryPlayerCarIndex = data[11]
    
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