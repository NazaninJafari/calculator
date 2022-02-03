from cmath import sqrt
import math

a = float (input ("enter first number:"))

op = input ("che amali (+ , - , * , / , sin, cos, tavan, jazr): ")

if op == "+" :
    b = float(input("enter second number:"))
    result = a + b

if op == "-" :
    b = float(input("enter second number:"))
    result = a - b

if op == "*" :
    b = float(input("enter second number:"))
    result = a * b

if op == "/" :
    b = float(input("enter second number:"))
    if b != 0 :
        result = a / b
    else :
        print ("error")    
    
if op == "sin" :
    x = math.sin(a)
    result = x 

if op == "cos" :
    x = math.cos(a)
    result = x

if op == "tavan" :
    result = a ** 2

if op == "jazr" :
    x = math.sqrt(a)
    result = x

print (result)
