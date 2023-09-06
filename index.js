
var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            var data = JSON.parse(event.data);
            console.log(data.header.packetId);
            //redirect(data);
        }

var participants;
var carSetup;
var carStatus;
var carTelemetry;
var carDamage;

function showModuleSelector(t) {
    t.innerHTML = moduleSelector_HTMLFILE;
    t.removeAttribute("onclick");
    console.log("called");
}

function showModule(t,moduleVar) {
    t.innerHTML = moduleVar;
}

function leaveModule(module) {
    showModuleSelector(module.parentNode.parentNode.parentNode);
}


function redirect(data) {
    switch(data.header.packetId) {
        case "0": 
            break;
        case "1":
            break;
        case "2":
            updateTower(data);
            break;
        case "3":
            addFIAevent(data);
            break;
        case "4":
            participants = data.participants;
            break;
        case "5":
            carSetup = data.carSetups[data.header.playerCarIndex];
            showSetupValues();
            break;
        case "6":
            // Car telemetry
            carTelemetry=data;
            updateTyreStatus();
            break;
        case "7":
            // Car status
            carStatus=data;
            updateTyreStatus();
            break;
        case "8":
            break;
        case "9":
            break;
        case "10":
            // Car damage
            carDamage=data;
            updateTyreStatus();
            break;
        case "11":
            break;
        case "12":
            break;
        case "13":
            break;
        default:
            console.log("def");
            break;
    }
}