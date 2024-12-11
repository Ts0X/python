
def sin():
    print(x+y)
def meion():
    print(x-y)  
def plus():
    print(x*y)
def dia():
    print(x/y)

x = float(input("enter first num: "))
y = float(input("enter second num:"))
z = input("enter +-*/")
if z == "+":
    sin()
elif z == "-":
    meion()
elif z == "*":
    plus()
elif z == "/":
    dia()
else:
    print("Invalid input")
