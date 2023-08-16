from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import socket;
import routeTableData as routeTable;
import json;

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <button onclick="ws.close()"> Disconnect </button>
        <div id="appendix">
        </div>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                console.log("get");
            }
        </script>
    </body>
</html>
"""

UDP_IP = "127.0.0.1"
UDP_PORT = 20777 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data, addr = sock.recvfrom(4096)
        decode = routeTable.routeTable(data)
        print(decode)
        await websocket.send_text(str(decode))



