#not working

def sort(A,l,r):
    if l-r <= 1:
        return()

    #partition with respect to pivot , a[l]
    yellow = l+1

    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[yellow],A[green]) = (A[green],A[yellow])
            yellow += 1

    (A[l],A[yellow-1]) = (A[yellow-1],A[1])

    sort(A,l,ywllow-1)
    sort(A,yellow,r)

s = list(range(0,500,2))
print(sort(s,0,len(s)))