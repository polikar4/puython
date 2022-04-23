import socket
from threading import Thread
from time import sleep
import sys

serv_sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock_send.bind(('', 53221))
serv_sock_send.listen(10)

potoki = []

vragi = [[1,1,1,0,0,0,12,"tt","info",1]]
resurs = [[5,5,5,0,0,0,1,"tt","info",2]]
igriki = [[3,3,3,0,0,0,12,"tt","info",3]]
bloki = [[8,5,8,0,0,0,12,"tt","info",4]]


def Otpravit_info(client_sock,mass,w):
    strr = w
    for i in mass:
        for j in i:
            strr += "|" + str(j)
        client_sock.sendall(str.encode(strr ,  encoding='utf-8'))
        while True:
            data = client_sock.recv(1024) 
            if(data.decode('UTF-8') == "ok"):
                break
        strr = w  
        


def rabota_s_klientom_send(client_sock, client_addr):
    Otpravit_info(client_sock,vragi,"v")
    Otpravit_info(client_sock,resurs,"r")
    Otpravit_info(client_sock,igriki,"i")
    Otpravit_info(client_sock,bloki,"b")
    client_sock.sendall(str.encode("Go" ,  encoding='utf-8'))
    
    
    while True:
        stroka = client_sock.recv(1024).decode('UTF-8')
        index = stroka.find("@")
        if( -1 != index):
            stroka.replace("@","")
            # функция отправки
        if( len(stroka) != 0):
            a = 5
            # фунция впитывания

    client_sock.close()    
    


def Exit():
    while True:
        if(input() == 0):
            sys.exit



def main():
    th = Thread(target=Exit, args = ())
    th.start()       
    while True:
        client_sock_send, client_addr_send = serv_sock_send.accept()
        print('Connected by', client_addr_send)
        th = Thread(target=rabota_s_klientom_send, args = (client_sock_send,client_addr_send,))
        th.start()        
        potoki.append(th)     
        
        for i in potoki:
            if(not i.isAlive):
                del i
                print("del")
                






if __name__ == "__main__":
    main()







