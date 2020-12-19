"""
gcd(m,n) ...where m>n
suppose d divides both m,n and m=ad,n=bd where a,b are some multiples
Then m-n= ad-bd= (a-b)d

If m > n
The problem can be reduced as
1) If n divides m, return n
2) Else, gcd(n,m-n) and return gcd ans

"""

def gcd(m,n):
    if m < n:
        (m,n) = (n,m)

    if(m%n == 0):
        return n
    else:
        return (gcd(max(n,m-n),min(n,m-n)))

n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

g = gcd(n1,n2)
print("GCD :",g)
