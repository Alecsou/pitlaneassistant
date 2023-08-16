import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class CarMotionData:
    def __init__(self,data):
        self.worldPositionX = data[0]
        self.worldPositionY = data[1]
        self.worldPositionZ = data[2]
        self.worldVelocityX = data[3]
        self.worldVelocityY = data[4]
        self.worldVelocityZ = data[5]
        self.worldForwwardX = data[6]
        self.worldForwwardY = data[7]
        self.worldForwwardZ = data[8]
        self.worldRightDirX = data[9]
        self.worldRightDirY = data[10]
        self.worldRightDirZ = data[11]
        self.gForceLateral = data[12]
        self.gForceLongitudinal = data[13]
        self.gForceVertical = data[14]
        self.yaw = data[15]
        self.pitch = data[16]
        self.roll = data[17]

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
    packet=[]
    tmp = 0
    for _ in range(6):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    for _ in range(6):
        data,tmp = pt.getSigned(data,16)
        packet.append(tmp)
    for _ in range(6):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    return data,CarMotionData(packet)

        

