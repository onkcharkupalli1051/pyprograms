#put small nos. to left of list... takes O(nlogn) time

def quick(A,l,r):
    if r-l < 1:
        return()

    yellow = l+1

    for green in range(l+1,r):
        if A[green] <= A[l]:
            A[yellow],A[green] = A[green],A[yellow]
            yellow += 1

    A[l],A[yellow-1] = A[yellow-1],A[l]

    quick(A,l,yellow-1)
    quick(A,yellow,r)

l = [91,22,45,98,66,54,787]
print(quick([l],0,len(l)-1))