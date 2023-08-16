import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class PacketMotionExData:
    def __init__(self,data):
        self.header = data[0]
        self.suspensionPosition = data[1]
        self.suspensionVelocity = data[2]
        self.suspensionAcceleration = data[3]
        self.wheelSpeed = data[4]
        self.wheelSlipRatio = data[5] 
        self.wheelSlipAngle = data[6] 
        self.wheelLatForce = data[7]
        self.wheelLongForce = data[8]
        self.heightOfCOGAboveGround = data[9] 
        self.localVelocityX = data[10] 
        self.localVelocityY = data[11]
        self.localVelocityZ = data[12] 
        self.angularVelocityX = data[13] 
        self.angularVelocityY = data[14]
        self.angularVelocityZ = data[15]
        self.angularAccelerationX = data[16] 
        self.angularAccelerationY = data[17] 
        self.angularAccelerationZ = data[18] 
        self.frontWheelsAngle = data[19]
        self.wheelVertForce = data[20]
    
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

def decode(data,header):
    packet = [header]
    tmp = 0
    for _ in range(8):
        tab = []
        for _ in range(4):
            data,tmp = pt.getFloat(data)
            tab.append(tmp)
        packet.append(tab)
    for _ in range(11):
        data,tmp = pt.getFloat(data)
        packet.append(tmp)
    tab = []
    for _ in range(4):
        data,tmp = pt.getFloat(data)
        tab.append(tmp)
    packet.append(tab)
    return PacketMotionExData(packet)
        
    

