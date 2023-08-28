
var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            var data = JSON.parse(event.data);
            console.log(data.header.packetId);
        }

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
