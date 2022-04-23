import socket
from time import sleep



client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('82.146.57.182', 53220))



while True:
    data = client_sock.recv(1024)
    if(len(data) != 0):
        print(data, len(data))
        client_sock.sendall(str.encode("ok" ,  encoding='utf-8'))
    print("", end = "")



