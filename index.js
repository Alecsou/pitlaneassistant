var ws = new WebSocket("ws://localhost:8000/ws");
        ws.onmessage = function(event) {
            console.log("get");
        }
