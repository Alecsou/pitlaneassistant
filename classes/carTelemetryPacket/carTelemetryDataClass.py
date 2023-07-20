import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

class CarTelemetryData:
    def __init__(self,data):
        self.speed = data[0]
        self.throttle = data[1] 
        self.steer = data[2] 
        self.brake = data[3]
        self.clutch = data[4]
        self.gear = data[5]
        self.engineRPM = data[6]
        self.drs = data[7]
        self.revLightsPercent = data[8]
        self.revLightsBitValue = data[9]
        self.brakesTemperature = data[10] 
        self.tyresSurfaceTemperature = data[11] 
        self.tyresInnerTemperature = data[12]
        self.engineTemperature = data[13]
        self.tyresPressure = data[14]
        self.surfaceType = data[15]


    def __str__(self):
        return str(vars(self))

def decode(data):
    packet = []
    tmp = 0
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    for _ in range(3):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getSigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,16)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
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
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    return data,CarTelemetryData(packet)
