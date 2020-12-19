def ss(l):
    for i in range(len(l)):
        min = i

        for j in range(i+1,len(l)):
            if l[min] > l[j]:
                min,j = j,min

        l[i], l[min] = l[min],l[i]
    return l

l = list(range(5,0,-1))
print(ss(l))


def selection_sort(l):
    for i in range(len(l)):
        min = i

        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j

        l[min], l[i] = l[i],l[min]
    return l

print(selection_sort([9,8,7,6,5,4,3,2,1]))