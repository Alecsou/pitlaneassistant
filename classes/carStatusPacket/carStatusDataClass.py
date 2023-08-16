import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class CarStatusData:
    def __init__(self,data):
        self.tractionControl = data[0]
        self.antiLockBrakes = data[1] 
        self.fuelMix = data[2] 
        self.frontBrakeBias = data[3] 
        self.pitLimiterStatus = data[4]
        self.fuelInTank = data[5]
        self.fuelCapacity = data[6]
        self.fuelRemainingLaps = data[7]
        self.maxRPM = data[8]
        self.idleRPM = data[9] 
        self.maxGears = data[10]
        self.drsAllowed = data[11] 
        self.drsActivationDistance = data[12] 
        self.actualTyreCompound = data[13] 
        self.visualTyreCompound = data[14]
        self.tyresAgeLaps = data[15]
        self.vehicleFiaFlags = data[16]
        self.enginePowerICE = data[17]
        self.enginePowerMGUK = data[18] 
        self.ersStoreEnergy = data[19]
        self.ersDeployMode = data[20]
        self.ersHarvestedThisLapMGUK = data[21] 
        self.ersHarvestedThisLapMGUH = data[22] 
        self.ersDeployedThisLap = data[23]
        self.networkPaused = data[24]

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
    for _ in range(5):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    data,tmp = pt.getSigned(data,8)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,CarStatusData(packet)
    