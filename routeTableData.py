import headerDecode as hd;
import importAll as ia;

def routeTable(data) :
    data,head = hd.headerDecode(data) 
    id = head.packetId
    match (id) :
        case 0:
            return ia.packetMotionData.decode(data,head)
        case 1:
            return ia.packetSessionData.decode(data,head) 
        case 2:
            return ia.packetLapData.decode(data,head) 
        case 3:
            return ia.packetEventData.decode(data,head) 
        case 4:
            return ia.packetParticipationData.decode(data,head)
        case 5:
            return ia.packetCarSetupData.decode(data,head) 
        case 6:
            return ia.packetCarTelemetryData.decode(data,head)
        case 7:
            return ia.packetCarStatusData.decode(data,head)
        case 8:
            return ia.packetFinalClassificationData.decode(data,head)
        case 9:
            return ia.packetLobbyInfoData.decode(data,head)
        case 10:
            return ia.packetCarDamageData.decode(data,head) 
        case 11:
            return ia.packetSessionData.decode(data,head)
        case 12:
            return ia.packetTyreSetData.decode(data,head)
        case 13:
            return ia.packetMotionExData.decode(data,head)
        case _:
            return "Error" 

