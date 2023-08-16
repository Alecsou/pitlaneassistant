import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class CarSetupData:
    def __init__(self,data):
        self.frontWing = data[0] 
        self.rearWing = data[1] 
        self.onThrottle = data[2]
        self.offThrottle = data[3] 
        self.frontCamber = data[4]
        self.rearCamber = data[5] 
        self.frontToe = data[6]
        self.rearToe = data[7] 
        self.frontSuspension = data[8] 
        self.rearSuspension = data[9] 
        self.frontAntiRollBar = data[10]
        self.rearAntiRollBar = data[11]
        self.frontSuspensionHeight = data[12]
        self.rearSuspensionHeight = data[13]
        self.brakePressure = data[14] 
        self.brakeBias = data[15]
        self.rearLeftTyrePressure = data[16] 
        self.rearRightTyrePressure = data[17] 
        self.frontLeftTyrePressure = data[18] 
        self.frontRightTyrePressure = data[19] 
        self.ballast = data[20] 
        self.fuelLoad = data[21] 

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
    for _ in range(4):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(4):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    for _ in range(8):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    for _ in range(4):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    data,tmp = pt.getUnsigned(data,8)
    packet.append(tmp)
    data,tmp = pt.getFloat(data)
    packet.append(tmp)
    return data,CarSetupData(packet)