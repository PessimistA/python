from asyncio import timeout

import requests

url = "xxx"
header = {'user-agent':'isim/1.1.1'}
#r = requests.get(url)#bu temel hali


#r = requests.get(url,headers=header,allow_redirect=True,timeout=2)#false olursa request göndermesine izin vermez 404 300 gibi değerler döner

print(r.status_code)#hatayı veya girilebiliyorsa doğru değeri döndürür
print(r.text)#sayfanın html java kodlarını bastırır

#timeout bu süre içinde geri döndürme sağlamasını ister