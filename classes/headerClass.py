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
        return str(vars(self))