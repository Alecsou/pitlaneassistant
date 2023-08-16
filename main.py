import socket;
import rawToBin;
import routeTableData as routeTable;

UDP_IP = "127.0.0.1"
UDP_PORT = 20777 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while (True):
    data, addr = sock.recvfrom(4096)
    decode = routeTable.routeTable(rawToBin.rawToBin(data))
    print(decode)
