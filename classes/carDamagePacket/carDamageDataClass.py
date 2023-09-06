import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import inspect;

class CarDamageData:
    def __init__(self,data):
        self.tyresWear = data[0]
        self.tyresDamage = data[1] 
        self.brakesDamage = data[2]
        self.frontLeftWingDamage = data[3] 
        self.frontRightWingDamage = data[4] 
        self.rearWingDamage = data[5] 
        self.floorDamage = data[6] 
        self.diffuserDamage = data[7] 
        self.sidepodDamage = data[8] 
        self.drsFault = data[9] 
        self.ersFault = data[10]
        self.gearBoxDamage = data[11]
        self.engineDamage = data[12]
        self.engineMGUHWear = data[13]
        self.engineESWear = data[14] 
        self.engineCEWear = data[15] 
        self.engineICEWear = data[16] 
        self.engineMGUKWear = data[17]
        self.engineTCWear = data[18] 
        self.engineBlown = data[19] 
        self.engineSeized = data[20]

    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    tab = []
    for _ in range(4):
        data,tmp = pt.getFloat(data)
        tab.append(tmp)
    packet.append(tab)
    tab = []
    for _ in range(4):
        data,tmp = pt.getUnsigned(data,8)
        tab.append(tmp)
    packet.append(tab)
    tab = []
    for _ in range(4):
        data,tmp = pt.getUnsigned(data,8)
        tab.append(tmp)
    packet.append(tab)
    for _ in range(18):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data,CarDamageData(packet)