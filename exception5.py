try:
    x=int(input("Enter firtst number"))
    y=int(input("Enter second number"))  
    print(x/y)   
except ZeroDivisionError:
    print("Arif")
    print("Hello this line is last line")
try:
    x=int(input("Enter firtst number"))
    y=int(input("Enter second number"))  
    print(x/y)   
except TypeError:
    print("Arif")
finally:
    print("In finally") 