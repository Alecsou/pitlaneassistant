
var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            //console.log(event.data);
            if (event.data=="OSEF") {return;}
            var data = JSON.parse(event.data);
            redirect(data);
        }

var participants;
var carSetup;
var carStatus;
var carTelemetry;
var carDamage;
var session;
var lapData;
var lapDataHistory = Array(24).fill(undefined);
var driverCarIdx;

function showModuleSelector(t) {
    t.innerHTML = moduleSelector_HTMLFILE;
    t.removeAttribute("onclick");
}

function showModule(t,moduleVar) {
    t.innerHTML = moduleVar;
    t.setAttribute("onclick","");
}

function leaveModule(module) {
    showModuleSelector(module.parentNode.parentNode.parentNode);
}


function redirect(data) {
    driverCarIdx = data.header.playerCarIndex;
    switch(data.header.packetId) {
        case "0": 
            break;
        case "1":
            session = data;
            //updateWeather();
            updateHeader();
            updateClockMap();
            updateCarStatus();
            break;
        case "2":
            lapData = data
            updateTower(lapData);
            updateDriverLine();
            break;
        case "3":
            addFIAevent(data);
            break;
        case "4":
            participants = data.participants;
            break;
        case "5":
            carSetup = data.carSetups[data.header.playerCarIndex];
            //showSetupValues();
            break;
        case "6":
            // Car telemetry
            carTelemetry=data;
            updateTyreStatus();
            updateDamage();
            break;
        case "7":
            // Car status
            carStatus=data;
            updateTyreStatus();
            updateCarStatus();
            break;
        case "8":
            break;
        case "9":
            break;
        case "10":
            // Car damage
            carDamage=data;
            updateTyreStatus();
            updateDamage();
            break;
        case "11":
            lapDataHistory[data.carIdx]=data;
            updateTower();
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

function swapToScreen() {
    document.getElementById("boxes").style.right = "100%";
    document.getElementById("screen1").style.right = "0%";
}
function swapToBoxes() {
    document.getElementById("boxes").style.right = "0%";
    document.getElementById("screen1").style.right = "-100%";
}