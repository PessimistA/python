def asistan(command):
    if command=="date":
        date()
    elif command =="time":
        time()
    elif command =="adding":
        adding_note()

def date():
    from datetime import datetime
    print(f"date is {datetime.now().strftime("%d-%m-%Y")}")

def time():
    from datetime import datetime
    print(f"time is {datetime.now().strftime("%H:%M:%S")}")

def adding_note():
    print("Please give a name to your notepad")

    name = input()

    with open(f"{name}.txt","w") as file:
        print("you can write now (if you want to quit press enter)")
        file.write(input())

print("welcome to the asistane bot")
while 1:
    command = input("please write your command if you want to exit write 'exit'").lower()
    if command == "exit":
        break
    else:
        asistan(command)