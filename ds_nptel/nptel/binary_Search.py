def bs(li,x,f,l):
    if (l-f == 0):
        return False
    else:
        mid = ((l+f) // 2)
        print("list : ",li)
        print("mid : ",mid)
        print("li[mid] : ",li[mid])
        if li[mid] == x:
            return True
        elif(x < li[mid]):
            return (bs(li,x,f,mid))
        elif(x > li[mid]):
            return (bs(li,x,mid+1,l))

print(bs(list(range(1,10)),5,0,10))

