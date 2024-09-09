import socket

#ip adresi ve port tanıma
host ="xxx.x.x.x"#host ip ata random
port = 50001
#socket oluşturma ve sunucuya bağlama
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
#kullanıcıdan mesaj almak ve göndermek
message = input(">> ")
#Mesaj Gönderme ve Sunucudan Yanıt Alma Döngüsü
while message.lower().strip()!= "quit":
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("response from server : "+str(data))
    message +input(">> ")
#Bağlantıyı Kapatma
client_socket.close()