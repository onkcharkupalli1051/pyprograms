"""
def bs(l,x,start,end):
    while(end != start):
        mid = start+end//2
        if (x == l[mid]):
            print("Element found")
        elif (x < l[mid]):
            return bs(l,x,start,mid-1)
        elif x > l[mid]:
            return bs(l,x,mid+1,end)

"""
def bs(l,x,start,end):
    if start == end:
        if l[start] == x:
            return start
        else:
            return -1
    else:
        mid = int((start+end)/2)
        if l[mid] == x:
            print("mid")
            return mid
        elif l[mid] > x:
            return bs(l,x,start,mid-1)
        elif l[mid] < x:
            return bs(l,x,mid+1,end)

x = int(input("Enter element to found : "))
ls = list(range(1,10,2))
index = bs(ls,x,1,len(ls))
if index == -1:
    print(x,"not found")
else:
    print(x,"found at position",index)
