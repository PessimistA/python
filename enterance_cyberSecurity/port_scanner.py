//version 1 --> just scanner
import socket
from logging import exception

ip = input("enter ip idress")
timeout = float(input("enter a time limit"))
for port in range(1,5000):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        s.connect((ip,port))
        print(str(port),":open")
    except Exception as e:
        print(str(port),":closed")
        pass
    finally:
        s.close()

//version 2 --> return port's name
import socket
from logging import exception

ip = input("enter ip idress")
timeout = float(input("enter a time limit"))
lastrange = int(input("enter a limit for range"))

for port in range(1,lastrange):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        s.connect((ip,port))
        response = s.recv(1024)

        print(str(port),":open : Banner :",response.decode())
    except Exception as e:
        print(str(port),":closed : reason :",str(e))
        pass
    finally:
        s.close()

//version 3 banner usage
import socket
from email.quoprimime import decode
from logging import exception

ip = input("enter ip idress")
timeout1 = float(input("enter a time limit"))
lastrange = int(input("enter a limit for range"))

for port in range(1,lastrange):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout1)
        s.connect((ip,port))
        response = s.recv(1024)

        print(str(port),":open : Banner :",response.decode())

    except socket.timeout as t:
        if(port ==80):
            httpmessage = "GET / HTTP/1.0\r\n\r\n"
            s.send(httpmessage.encode())
            httprecive= s.recv(1024)
            print(str(port),": open : Banner :",response(decode()))
        else:
            print(str(port),": user different method")

    except Exception as e:
        print(str(port),":closed : reason :",str(e))
        pass
    finally:
        s.close()

