def gcd(n1,n2):
    i = min(n1,n2)
    while(True):
        if n1%i == 0 and n2%i == 0:
            print("GCD : {}".format(i))
            exit(0)
        else:
            i -= 1

n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

print(gcd(n1,n2))