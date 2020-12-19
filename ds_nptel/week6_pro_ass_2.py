from math import pow

def check(n):
    if (n==0):
        return False
    while(n!=1):
        if(n%2!=0):
            return False
        n = n//2
    return True

n = int(input())

if check(n):
    print("YES")
else:
    print("NO")
