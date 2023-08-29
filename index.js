
var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            var data = JSON.parse(event.data);
            console.log(data.header.packetId);
            redirect(data);
        }

var carSetup;

function showModuleSelector(t) {
    t.innerHTML = moduleSelector_HTMLFILE;
    t.removeAttribute("onclick");
    console.log("called");
}

function showModule(t,moduleVar) {
    t.parentNode.parentNode.innerHTML = moduleVar;
}

function leaveModule(module) {
    showModuleSelector(module.parentNode.parentNode.parentNode);
}

function redirect(data) {
    console.log(data);
    console.log(data.header.packetId);
    switch(data.header.packetId) {
        case "0": 
            break;
        case "1":
            break;
        case "2":
            break;
        case "3":
            break;
        case "4":
            break;
        case "5":
            console.log(data.carSetups);
            console.log(data.header.playerCarIndex);
            console.log(data.carSetups[data.header.playerCarIndex]);
            carSetup = data.carSetups[data.header.playerCarIndex];
            showSetupValues();
            break;
        case "6":
            break;
        case "7":
            break;
        case "8":
            break;
        case "9":
            break;
        case "10":
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