from re import search

from scapy.all import RandMAC, RandIP, sendp
from scapy.layers.inet import IP, Ether 
from scapy.layers.l2 import Ether
from scapy.volatile import RandMAC, RandIP

pck_list = []
for i in range(10):
    source_mac = RandMAC()#random mac adresi
    destination_mac = RandMAC()
    source_ip = RandIP()#random ip adresi
    destination_ip = RandIP()

    ether = Ether(src=source_mac,dst=destination_mac)#src= source ||dst = destination
    ip = IP(src=source_ip,dst=destination_ip)
    packet = ether/ip
    pck_list.append(packet)
    print(source_mac,":",source_ip,">>",destination_mac,":",destination_ip)

sendp(pck_list,iface="eth0",verbose=False)#yanlışları çalıştırmasın false değeri girerim bu yüzden
