
var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            var data = JSON.parse(event.data);
            console.log(data.header.packetId);
        }

function showModuleSelector(t) {
    t.innerHTML = moduleSelector_HTMLFILE;
    t.removeAttribute("onclick");
}

function showModule(t,moduleVar) {
    console.log("ouais");
    t.parentNode.innerHTML = moduleVar;
}
