#version 1 --> tek bir sayfa için 
import requests
from bs4 import BeautifulSoup

#sayfanın hangi dil ile alınabileceğini araştır
url = input("bir url giriniz ")
response = requests.get(url)#html kodlarını alır

parser = BeautifulSoup(response.text,'html.parser')#html ile html parser ile yapman gerekir

etiket_name = input("almak istediğiniz etiket adını giriniz (bkn span,head)")
class_name = input("lütfen class ismini giriniz")
spans = parser.findAll(etiket_name, {"class": class_name})  # mesela span içindeki bir class için yaptın sonraısnda class ismini örnekteki gibi yazmalısın

for s in spans:
    print(s)
    print(s.text)  # bununla etiketin içeriğindeki text okunabilir olur
    title = s.find('h3',{"class":class_name})
    print(title)
    print(title['title'])#bununla başlayanları yazdır manasında
    #print(s.text)#bununla etiketin içeriğindeki text okunabilir olur

#version 2 --> birden fazla sayfa için

import requests
from bs4 import BeautifulSoup

#sayfanın hangi dil ile alınabileceğini araştır
url = input("bir url giriniz ")
range_limit = int(input("please enter a range limit"))
for i in range(range_limit):
    url21 =input("enter your url please").split("page=")
    if len(url21) > 1:
        url2 = url21[0] + "page=" + str(i) + url21[1]#sayfanın ortasında ise
    else:
        url2 = url21[0] + "page=" + str(i)#sayfanın sonunda sayı varsa

    response = requests.get(url)#html kodlarını alır

    parser = BeautifulSoup(response.text,'html.parser')#html ile html parser ile yapman gerekir

    etiket_name = input("almak istediğiniz etiket adını giriniz (bkn span,head)")
    class_name = input("lütfen class ismini giriniz")
    spans = parser.findAll(etiket_name, {"class": class_name})  # mesela span içindeki bir class için yaptın sonraısnda class ismini örnekteki gibi yazmalısın
    finding = input("bulunmasını istediğiniz etiketi giriniz");
    finding2 = input("bulunmasını istediğiniz yazıyı giriniz")
    for s in spans:
        print(s)
        #print(s.text)  # bununla etiketin içeriğindeki text okunabilir olur
        #title = s.find(finding,{"class":class_name})
        #print(title)
        #print(title[finding2])#bununla başlayanları yazdır manasında
        #print(s.text)#bununla etiketin içeriğindeki text okunabilir 
