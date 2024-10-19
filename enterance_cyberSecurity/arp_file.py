import argparse
from scapy import all as scapy

class arp_ping():
    def __init__(self):
        print("arp ping başlatıldı")
    def user_input_take(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('-i', '--ipadress', type=str, help="İP adresinizi giriniz")

        args = parser.parse_args()

        print(args.ipadress)

        if args.ipadress != None:
            return args
        else:
            print("ip adresini -i argümanıyla giriniz")

    def arp_request(self,ip):
        ans,unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip),timeout=1)
        ans.summary()

if __name__ == "__main__":
    arp_ping1 = arp_ping()
    user_ping = arp_ping1.user_input_take()
    arp_ping1.arp_request(user_ping.ipadress)
