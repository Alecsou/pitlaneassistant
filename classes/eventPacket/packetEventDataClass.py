import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import parseTypes as pt;

import classes.eventPacket.buttonsClass as buttons
import classes.eventPacket.driveThroughPenaltyServedClass as driveThroughPenaltyServed
import classes.eventPacket.fastestLapClass as fastestLap
import classes.eventPacket.flashbackClass as flashback
import classes.eventPacket.overtakeClass as overtake
import classes.eventPacket.penaltyClass as penalty
import classes.eventPacket.raceWinnerClass as raceWinner
import classes.eventPacket.retirementClass as retirement
import classes.eventPacket.speedTrapClass as speedTrap
import classes.eventPacket.startLightsClass as startLights
import classes.eventPacket.stopGoPenaltyServedClass as stopGoPenaltyServed
import classes.eventPacket.teamMateInPitsClass as teamMateInPits

import inspect;

class PacketEventData:
    def __init__(self, data):
        self.header = data[0]
        self.eventStringCode = data[1]
        self.eventDetails = data[2]
    
    def __str__(self):
        return pt.getStr(self)

def decode(data,header):
    packet = [header]
    tmp = 0
    message = []
    for _ in range(4):
        data,tmp = pt.getChar(data)
        message+=tmp
    packet.append(message);
    match (message):
        case "SSTA":
            data,tmp = data,"SSTA"
            packet.append(tmp)
        case "SEND":
            data,tmp = data,"SEND"
            packet.append(tmp)
        case "FTLP":
            data,tmp = fastestLap.decode(data)
            packet.append(tmp)
        case "RTMT":
            data,tmp = retirement.decode(data)
            packet.append(tmp)
        case "DRSE":
            data,tmp = data,"DRSE"
            packet.append(tmp)
        case "DRSD":
            data,tmp = data,"DRSD"
            packet.append(tmp)
        case "TMPT":
            data,tmp = teamMateInPits.decode(data)
            packet.append(tmp)
        case "CHQF":
            data,tmp = data,"CHQF"
            packet.append(tmp)
        case "RCWN":
            data,tmp = raceWinner.decode(data)
            packet.append(tmp)
        case "PENA":
            data,tmp = penalty.decode(data)
            packet.append(tmp)
        case "SPTP":
            data,tmp = speedTrap.decode(data)
            packet.append(tmp)
        case "STLG":
            data,tmp = startLights.decode(data)
            packet.append(tmp)
        case "LGOT":
            data,tmp = data,"LGOT"
            packet.append(tmp)
        case "DTSV":
            data,tmp = driveThroughPenaltyServed.decode(data)
            packet.append(tmp)
        case "SGSV":
            data,tmp = stopGoPenaltyServed.decode(data)
            packet.append(tmp)
        case "FLBK":
            data,tmp = flashback.decode(data)
            packet.append(tmp)
        case "BUTN":
            data,tmp = buttons.decode(data)
            packet.append(tmp)
        case "RDFL":
            data,tmp = data,"RDFL"
            packet.append(tmp)
        case "OVTK":
            data,tmp = overtake.decode(data)
            packet.append(tmp)
        case _:
            packet.append("ERROR")
    return PacketEventData(packet)
        
        

