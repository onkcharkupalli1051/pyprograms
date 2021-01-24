import random

ch = 1
while(ch == 1):
    x = random.randint(1,7)
    print("*******")
    print("*     *")
    print("* ",x," *")
    print("*     *")
    print("*******")
    ch = int(input("Enter 1 to continue : "))