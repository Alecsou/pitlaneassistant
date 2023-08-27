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
    styleFile = open("./index.css","r")
    style = styleFile.read()
    styleIdx = newindex.rfind("<style>")
    newindex = newindex[:styleIdx+len("<style>")]+style+newindex[styleIdx+len("<style>"):]
    return newindex

def include(file,tag):
    global html
    incFile = open(file,"r")
    content = incFile.read()
    contentIdx = html.rfind(tag)
    html = html[:contentIdx+len(tag)]+content+html[contentIdx+len(tag):]

def includeHTML(file):
    global html
    name = file[2:-5]
    incFile = open(file,"r")
    content = "'"+str(repr(incFile.read())[1:-1]).replace(r'\n', ' ')+"'"
    contentIdx = html.rfind("<script>")
    html = html[:contentIdx+len("<script>")]+"\n var "+name+"_HTMLFILE = "+content+html[contentIdx+len("<script>"):]

html = indexBuilder()
includeHTML("./setupModule.html")
includeHTML("./FIAeventModule.html")
includeHTML("./moduleSelector.html")

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



