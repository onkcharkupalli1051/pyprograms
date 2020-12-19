"""def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        while(n>1):
            c = a + b
            a = b
            b = c
            n -= 1
    return c
"""
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        value = fib(n-1) + fib(n-2)
    return value

print(fib(6))
