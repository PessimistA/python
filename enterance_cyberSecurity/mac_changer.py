import random
import subprocess
from logging.config import fileConfig
import re

charlist = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']

newmac= ""

for i in range(12):
    newmac = newmac +random.choice(charlist)
print(newmac)

ifconfigresult = subprocess.check_output("ifconfig eth0", shell=True).decode()
print(ifconfigresult)

oldmac = re.search("ether(.*?)txqueuelen",ifconfigresult).group(1).strip()
print("old mac: ",oldmac)

subprocess.check_output("ifconfig eth0 down",shell=True)
subprocess.check_output("ifconfig eth0 hw ether " + newmac, shell=True)
subprocess.check_output("ifconfig eth0 up",shell=True)

ifconfigresult2 = subprocess.check_output("ifconfig eth0", shell=True).decode()
print("last ifconfig result",ifconfigresult2)
