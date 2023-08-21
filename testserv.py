from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import socket;
import routeTableData as routeTable;
import json;

app = FastAPI()

def indexBuilder() :
    indexFile = open("./index.html","r")
    scriptFile = open("./index.js","r")
    index = indexFile.read()
    script = scriptFile.read()
    scriptIdx = index.rfind("<script>")
    newindex = index[:scriptIdx+len("<script>")]+script+index[scriptIdx+len("<script>"):]
    return newindex

html = indexBuilder()

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



