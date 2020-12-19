"""
Dynamic Programming :
Dividing a problem into smaller sub-problems,Instead of going
through the recursive calls, anticipate what the memory table looks like.
The sub-problems result directly affects the main problem.
Must be acylic.

k      : 0 1 2 3 4 5
fib(k) :
"""
def fibtable(n):
    fibtable[0] = 0
    fibtable[1] = 1
    for i in range(2,n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]
    return (fibtable[n])
