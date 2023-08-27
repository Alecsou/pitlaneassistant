import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import classes.sessionPacket.marshalZoneClass as marshalZone;
import classes.sessionPacket.weatherForecastSampleClass as weatherForecastSample;
import inspect;

class PacketSessionData:
    def __init__(self,data):
        self.header = data[0]
        self.weather = data[1]
        self.trackTemperature = data[2]
        self.airTemperature = data[3]
        self.totalLaps = data[4]
        self.trackLength = data[5]
        self.sessionType = data[6]
        self.trackId = data[7]
        self.formula = data[8]
        self.sessionTimeLeft = data[9]
        self.sessionDuration = data[10]
        self.pitSpeedLimit = data[11]
        self.gamePaused = data[12]
        self.isSpectating = data[13]
        self.spectatorCarIndex = data[14]
        self.sliProNativeSupport = data[15]
        self.numMarshalZones = data[16]
        self.marshalZones = data[17]
        self.safetyCarStatus = data[18]
        self.networkGame = data[19]
        self.numWeatherForecastSamples = data[20]
        self.weatherForecastSamples = data[21]
        self.forecastAccuracy  = data[22]
        self.aiDifficulty = data[23]
        self.seasonLinkIdentifier = data[24]  
        self.weekendLinkIdentifier = data[25]  
        self.sessionLinkIdentifier = data[26]
        self.pitStopWindowIdealLap = data[27]
        self.pitStopWindowLatestLap = data[28]
        self.pitStopRejoinPosition = data[29]
        self.steeringAssist = data[30]
        self.brakingAssist = data[31]
        self.gearboxAssist = data[32]
        self.pitAssist = data[33]
        self.pitReleaseAssist = data[34]
        self.ERSAssist = data[35]
        self.DRSAssist = data[36]
        self.dynamicRacingLine = data[37]
        self.dynamicRacingLineType = data[38]
        self.gameMode = data[39]
        self.ruleSet = data[40]
        self.timeOfDay = data[41]
        self.sessionLength = data[42]
        self.speedUnitsLeadPlayer = data[43]
        self.temperatureUnitsLeadPlayer = data[44]
        self.speedUnitsSecondaryPlayer = data[45]
        self.temperatureUnitsSecondaryPlayer = data[46]
        self.numSafetyCarPeriods = data[47]
        self.numVirtualSafetyCarPeriods = data[48]
        self.numRedFlagPeriods = data[49]
    
    def __str__(self):
        return pt.getStr(self)
    
def decode(data,header):
    packet = [header]
    tmp = 0
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    for _ in range(2):
        data,tmp = pt.getSigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getSigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,16)
        packet.append(tmp)
    for _ in range(6):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    marshalZones = []
    for _ in range(21):
        data,tmp = marshalZone.decode(data)
        marshalZones.append(tmp)
    packet.append(marshalZones)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    weather = []
    for _ in range(56):
        data,tmp = weatherForecastSample.decode(data)
        weather.append(tmp)
    packet.append(weather)
    for _ in range(2):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,32)
        packet.append(tmp)
    for _ in range(14):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    for _ in range(8):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return PacketSessionData(packet)