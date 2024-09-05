#password maker
import random
password = ""
symbols = []
long = int(input("please enter your limit"))
x = 0
while 1:
    saving_spot = input("please enter symbols if you wanna quit please enter 'q' ")
    if saving_spot == 'q' or x >= long:
        break
    else:
        if saving_spot not in symbols: 
            symbols.append(saving_spot)
            x += 1

for i in range(long):
    if not symbols:
        break
    randomaze_number = random.randint(0,len(symbols)-1)
    randomaze_symbol = symbols.pop(randomaze_number)
    password = password + randomaze_symbol

print(password)