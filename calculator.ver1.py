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