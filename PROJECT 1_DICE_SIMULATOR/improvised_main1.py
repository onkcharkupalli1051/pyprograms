import random

ch = 1
while(ch == 1):
    n = random.randint(1,7)
    if n == 1:
        print("********")
        print("*      *")
        print("*  0   *")
        print("*      *")
        print("********")
    elif n == 2:
        print("********")
        print("*      *")
        print("* 0  0 *")
        print("*      *")
        print("********")
    if n == 3:
        print("*********")
        print("*       *")
        print("* 0 0 0 *")
        print("*       *")
        print("*********")
    if n == 4:
        print("*********")
        print("*       *")
        print("*  0 0  *")
        print("*  0 0  *")
        print("*       *")
        print("*********")
    if n == 5:
        print("********")
        print("* 0   0*")
        print("*   0  *")
        print("* 0   0*")
        print("********")
    if n == 6:
        print("*******")
        print("*0  0 *")
        print("*0  0 *")
        print("*0  0 *")
        print("*******")

    ch = int(input("Enter 1 to continue : "))