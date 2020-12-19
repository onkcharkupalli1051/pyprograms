# A and B list should be sorted

def mergesort(A,B):
    C = []

    m,n = len(A),len(B)

    i,j = 0,0

    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    return C

print(mergesort([1,5,7,9],[6,8,10]))


def practise(A,B):
    C = []

    m,n = len(A),len(B)

    i,j = 0,0

    while(i+j < m+n):
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    return C

print(practise([11,13,15],[12,14,16]))

#this function doesn't work
def merge2(A,B):
    C = []

    m, n = len(A), len(B)

    i, j = 0, 0

    while (i + j < m + n):

        #combine case 1 & 4
        if i == m or A[i] > B[j]:
            C.append(B[j])
            j += 1

        # combine case 2 & 3
        elif j == n or A[i] <= B[j]:
            C.append(A[i])
            i += 1
    return C

#function 3 : doesn't work
def merge3(A,left,right):

    if right-left <= 1:
        return (A[left:right])

    if right-left > 1:
        mid = (left+right//2)

        L = merge3(A,left,mid)
        R = merge3(A,mid,right)

    return A[left:right]

l3 = list(range(1,100,2)) + list(range(1,100,2))
print(merge3(l3,0,len(l3)))


