def fib(n):
    a = 0
    b = 1
    print(a,b,end = " ")
    while(n > 1):
        c = a + b
        print(c,end = " ")
        a = b
        b = c
        n = n-1
fib(5)