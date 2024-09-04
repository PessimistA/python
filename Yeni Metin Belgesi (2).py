print("Hello to the notepad")
print("Please give a name to your notepad")

name = input()

with open(f"{name}.txt","w") as file:
    print("you can write now if you want to quit press enter")
    file.write(input())

print("if you want to quit please press 'q' if you want to keep going press 'y'")
question =input().lower()

if question== 'q':
    print("see you soon")
elif question =='y':
    print("for reading what you have write press 1"+
          "for adding stuff on it press 2 ")
    question2 = input()
    if question2 =='1':
        with open(f"{name}.txt","r") as file2:
            print("if you want to read everything please press 1 "+
                  "if you want to read spesific line please press 2")
            question3 =input()
            if question3 =='1':
                whole_file = file2.read
                print(whole_file)
            elif question3 =='2':
                line_number= input("please enter your line number")
                lines = file2.readlines()
                lines_lenght = len(lines)
                for i in range(0,lines_lenght):
                    if i== int(line_number):
                        wanted = lines[i-1]
                        print(wanted)
    if question2 == '2':
        with open(f"{name}.txt","a") as file3:
            adding_stuff = input("please write what you wanna add")
            file3.write(adding_stuff)
        with open(f"{name}.txt","r") as file4:
            last_version = file4.read()
            print(last_version)


