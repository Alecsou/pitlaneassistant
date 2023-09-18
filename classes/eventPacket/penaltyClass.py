import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;
import specificID as sid;
import inspect;

class Penalty:
    def __init__(self,data):
        self.penaltyType = data[0]
        self.infringementType = data[1] 
        self.vehicleIdx = data[2]
        self.otherVehicleIdx = data[3]
        self.time = data[4] 
        self.lapNum = data[5] 
        self.placesGained = data[6]
        self.penaltyName = sid.penaltyID(data[0])
        self.infringementName = sid.infrigementID(data[1])
    
    def __str__(self):
        return pt.getStr(self)

def decode(data):
    packet = []
    tmp = 0
    for _ in range(7):
        data,tmp = pt.getUnsigned(data,8)
        packet.append(tmp)
    return data,Penalty(packet)