"""
#recursive
def fact(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n*(fact(n-1)))
    else:
        print("Invalid No.")"""

#iterative
def fact(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

num = int(input("Enter the no : "))
print(fact(num))