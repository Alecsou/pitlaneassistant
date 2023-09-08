import headerDecode as hd;
import importAll as ia;
import rawToBin;

##
#   Recieves the raw data from the UDP reciever and treats it accordingly
#   @param {Bytearray} data Bytearray of raw data coming from the UDP reciever
#   @returns {Class} A class containing the treated data in its right form
##
def routeTable(data) :
    size = len(data)
    data = rawToBin.rawToBin(data)
    match (size) :
        case 1349:
            data, head = hd.headerDecode(data)
            return ia.packetMotionData.decode(data,head)
        case 644:
            data, head = hd.headerDecode(data)
            return ia.packetSessionData.decode(data,head) 
        case 1131:
            data, head = hd.headerDecode(data)
            return ia.packetLapData.decode(data,head) 
        case 45:
            data, head = hd.headerDecode(data)
            return ia.packetEventData.decode(data,head) 
        case 1306:
            data, head = hd.headerDecode(data)
            return ia.packetParticipationData.decode(data,head)
        case 1107:
            data, head = hd.headerDecode(data)
            return ia.packetCarSetupData.decode(data,head) 
        case 1352:
            data, head = hd.headerDecode(data)
            return ia.packetCarTelemetryData.decode(data,head)
        case 1239:
            data, head = hd.headerDecode(data)
            return ia.packetCarStatusData.decode(data,head)
        case 1020:
            data, head = hd.headerDecode(data)
            return ia.packetFinalClassificationData.decode(data,head)
        case 1218:
            data, head = hd.headerDecode(data)
            return ia.packetLobbyInfoData.decode(data,head)
        case 953:
            data, head = hd.headerDecode(data)
            return ia.packetCarDamageData.decode(data,head) 
        case 1460:
            data, head = hd.headerDecode(data)
            return ia.packetSessionData.decode(data,head)
        case 231:
            data, head = hd.headerDecode(data)
            return ia.packetTyreSetData.decode(data,head)
        case 217:
            return "OSEF"
            return ia.packetMotionExData.decode(data,head)
        case _:
            return "Error" 

