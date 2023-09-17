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
    name = file[file.rfind("/")+1:-5]
    incFile = open(file,"r")
    content = "'"+str(repr(incFile.read())[1:-1]).replace(r'\n', ' ')+"'"
    contentIdx = html.rfind("<script id='htmlIncluder'>")
    html = html[:contentIdx+len("<script id='htmlIncluder'>")]+"\n var "+name+"_HTMLFILE = "+content+html[contentIdx+len("<script id='htmlIncluder'>"):]

html = indexBuilder()
includeHTML("./modules/html/moduleSelector.html")
includeHTML("./modules/html/setupModule.html")
includeHTML("./modules/html/FIAeventModule.html")
includeHTML("./modules/html/tyreStatusModule.html")
includeHTML("./modules/html/weatherModule.html")
includeHTML("./modules/html/towerModule.html")
includeHTML("./modules/html/damageModule.html")
includeHTML("./modules/html/carStatusModule.html")
includeHTML("./modules/html/clockMapModule.html")
include("./modules/js/setupModule.js","<script>")
include("./modules/js/weatherModule.js","<script>")
include("./modules/js/FIAeventModule.js","<script>")
include("./modules/js/towerModule.js","<script>")
include("./modules/js/tyreStatusModule.js","<script>")
include("./modules/js/damageModule.js","<script>")
include("./modules/js/carStatusModule.js","<script>")
include("./modules/js/clockMapModule.js","<script>")
include("./modules/js/header.js","<script>")


UDP_IP = "192.168.1.65"
UDP_PORT = 45023
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
        await websocket.send_text(str(decode))



