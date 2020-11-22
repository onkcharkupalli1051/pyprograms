def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def modulus(a,b):
    return a%b

while(True):
    a = float(input("Enter num1 : "))
    b = float(input("Enter num2 : "))
    print("\nOperations :\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus")
    ch = input("\nEnter choice : ")
    if ch == "1":
        print("\nAddition of {} and {} : {} ".format(a,b,addition(a,b)))
    elif ch == "2":
        print("\nSubtraction of {} and {} : {}  ".format(a,b,subtraction(a,b)))
    elif ch == "3":
        print("\nMultiplication of {} and {} : {} ".format(a,b,multiplication(a,b)))
    elif ch == "4":
        print("\nDivision of {} and {} : {} ".format(a,b,division(a,b)))
    elif ch == "5":
        print("\n Modulus of {} and {} : {}".format(a,b,modulus(a,b)))
    else:
        print("Invalid Choice")
