import headerDecode as hd;
import importAll as ia;

### CHECK case 0/1/2 : mauvais encodage des tableaux !!
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
            return "Final Classification" 
        case 9:
            return "Lobby Info" 
        case 10:
            return "Car Damage" 
        case 11:
            return "Session History" 
        case 12:
            return "Tyre Sets" 
        case 13:
            return "Motion Ex" 
        case _:
            return "Error" 

