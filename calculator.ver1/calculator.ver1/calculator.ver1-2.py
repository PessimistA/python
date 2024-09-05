class calculater:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def addition(self):
        print(int(self.x)+int(self.y))

    def subtraction(self):
        print(int(self.x)-int(self.y))

    def multiple(self):
        print(int(self.x)*int(self.y))
    
    def divide(self):
        if self.y != 0:
            print(int(self.x)/int(self.y))
        else:
            print("this divide cant be occured")
            

operator = input("please choose a operator '+' '-' '*' '/' ")
a = input("please enter a number: ")
b = input("please enter the second number: ")
operation = calculater(a,b)
if operator == '+':
    operation.addition()
if operator == '-':
    operation.subtraction()
if operator == '*':
    operation.multiple()
if operator == '/':
    operation.divide()
while 1:
    choose = input("if you want to quit press 'q' for the move on press 'm' ").lower()
    if choose== 'q':
        break
    elif choose == 'm':
        operator = input("please choose a operator '+' '-' '*' '/' ")
        a = input("please enter a number: ")
        b = input("please enter the second number: ")
        operation = calculater(a,b)
        if operator == '+':
            operation.addition()
        if operator == '-':
            operation.subtraction()
        if operator == '*':
            operation.multiple()
        if operator == '/':
            operation.divide()
    else:
        print("you entered wrong value")
#ver2 starts from here its dinamic version

def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiple(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "unable to do"
    return a / b
def calculator():
    answer = int(input("enter the number: "))
    while 1:
        print("choose the operation you wanted to do:")
        print("addition (+)")
        print("subtract (-)")
        print("multiplication (*)")
        print("division (/)")
        print("İşlemi bitirmek için 'q' yazın.")

        operation = input("Seçiminiz (+|-|/|*|q): ").lower()
        if operation =='q':
            print(f"{answer}")
            break
        else:
            number = int(input("enter the number: "))

            if operation =='+':
                answer = addition(answer,number)
            if operation =='-':
                answer = subtract(answer,number)
            if operation =='*':
                answer = multiple(answer,number)
            if operation =='/':
                answer = divide(answer,number)
calculator()
