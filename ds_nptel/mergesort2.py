#not working

def merge(a,left,right):
    if right-left <= 1:
        return a[left:right]
    elif right-left > 1:
        mid = (right+left)//2

        l = merge(a,left,mid)
        r = merge(a,mid,right)
        return(merge(a,l,r))

a = range(0,100,2)
b = list(range(1,100,2))
print(merge(a,0,len(a)))