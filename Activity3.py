num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
def add(x,y):
   return x+y
def sub(x,y):
   return x-y
def mul(x,y):
   return x*y
def quo(x,y):
   return x/y
def rem(x,y):
   return x%y
print("Addition", add(num1,num2))
print("Subtraction", sub(num1,num2))
print("Multiplication", mul(num1,num2))
print("Quotient", quo(num1,num2))
print("Remainder", rem(num1,num2))