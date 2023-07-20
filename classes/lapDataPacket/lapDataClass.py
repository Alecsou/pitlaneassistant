import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class LapData:
    def __init__(self,data):
        self.lastLapTimeInMS = data[0]
        self.currentLapTimeInMS = data[1]
        self.sector1TimeInMS = data[2]
        self.sector1TimeMinutes = data[3]
        self.sector2TimeInMS = data[4]
        self.sector2TimeMinutes = data[5]
        self.deltaToCarInFrontInMS = data[6]
        self.deltaToRaceLeaderInMS = data[7]
        self.lapDistance = data[8]
        self.totalDistance = data[9]
        self.safetyCarDelta = data[10]
        self.carPosition = data[11] 
        self.currentLapNum = data[12]  
        self.pitStatus = data[13]
        self.numPitStops = data[14]
        self.sector = data[15]
        self.currentLapInvalid = data[16]
        self.penalties = data[17]
        self.totalWarnings = data[18]
        self.cornerCuttingWarnings = data[19]
        self.numUnservedDriveThroughPens = data[20]
        self.numUnservedStopGoPens = data[21]
        self.gridPosition = data[22]
        self.driverStatus = data[23]
        self.resultStatus = data[24]
        self.pitLaneTimerActive = data[25]
        self.pitLaneTimeInLaneInMS = data[26]
        self.pitStopTimerInMS = data[27]
        self.pitStopShouldServePen = data[28]

    def __str__(self):
        return str(vars(self))

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,32)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    for _ in range(15):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,LapData(packet)