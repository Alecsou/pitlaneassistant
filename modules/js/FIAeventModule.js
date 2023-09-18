
/**
 * Adds an event in the FIAeventModule console
 * @param {Object} event 
 */
function addFIAevent(event) {
    function addMessage(str,code="") {
        let node = document.createElement("div");
        node.setAttribute("class","messageFIAEVENTMODULE "+code);
        node.textContent = str;
        document.getElementById("consoleFIAEVENTMODULE").prepend(node);
    }
    function timeFormat(time){
        var ms = (time - Math.floor(time)).toFixed(3).substring(1);
        var s = (Math.floor(time)%60).toString();
        var m = Math.floor((Math.floor(time)/60));
        s=(s.length==1)?"0"+s:s;
        return m+":"+s+ms;
    }
    switch (event.eventStringCode) {
        case "SSTA":
            addMessage(" > Session started ");
            break;
        case "SEND":
            addMessage(" > Session ended ");
            break;
        case "FTLP":
            addMessage(" > Fastest Lap : "+timeFormat(event.eventDetails.lapTime)+" by CAR index "+event.eventDetails.vehicleIdx,"FTLPFIAEVENTMODULE");
            break;
        case "RTMT":
            addMessage(" > Retirement : CAR index "+event.eventDetails.vehicleIdx)
            break;
        case "DRSE":
            addMessage(" > DRS Enabled ");
            break;
        case "DRSD":
            addMessage(" > DRS Disabled ");
            break;
        case "TMPT":
            addMessage(" > Teammate in pits ");
            break;
        case "CHQF":
            addMessage(" > CHEQEREDFLAG ","CHQFFIAEVENTMODULE");
            break;
        case "RCWN":
            addMessage(" > Race Winner : CAR index "+event.eventDetails.vehicleIdx,"RCWNFIAEVENTMODULE");
            break;
        case "PENA":
            addMessage(" > Penalty : CAR index "+event.eventDetails.vehicleIdx+", "+ event.eventDetails.infringementName+", "+event.eventDetails.penaltyName, "PENAFIAEVENTMODULE");
            break;
        case "SPTP":
            addMessage(" > Speed trap : CAR index "+event.eventDetails.vehicleIdx+", "+event.eventDetails.speed+" km/h");
            break;
        case "STLG":
            addMessage(" > Start sequence : "+event.eventDetails.numLights);
            break;
        case "LGOT":
            addMessage(" > LIGHTS OUT ","LGOTFIAEVENTMODULE");
            break;
        case "DTSV": 
            addMessage(" > Drive throught penalty served : CAR index "+event.eventDetails.vehicleIdx);
            break;
        case "SGSV":
            addMessage(" > Stop and Go penalty served : CAR index "+event.eventDetails.vehicleIdx);
            break; 
        case "FLBK":
            addMessage(" > FLASHBACK ACTIVATED");
            break;  
        case "BUTN":
            //addMessage(" > Button status changed : "+event.eventDetails.buttonStatus);
            break;
        case "RDFL":
            addMessage(" > RED FLAG ","RDFLFIAEVENTMODULE");
            break;
        case "OVTK":
            addMessage(" > Overtake : CAR index "+event.eventDetails.overtakingVehicleIdx+" on CAR index "+event.eventDetails.beingOvertakenVehicleIdx);
            break;
    }
}