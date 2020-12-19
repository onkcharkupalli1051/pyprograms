'''
rows = (0, R-1)
colums =(0,C-1)
start = (0,0)
No. of dragons = D
KIll = k
no. of dragons in row =  1+

'''
R,C,K,D = tuple(input().split())

R = int(R)
C= int(C)
K = int(K)
D = int(D)

dragons = []
for i in range(1,D+1):
    i = int(i)
    dragons.append(i)
print(dragons)

pos = []
for i in range(1,D+1):
    i,j = input().split()
    i = int(i)
    j = int(j)
    pos.append((i,j))
print(pos)

def mindist(i,j):
    for i in (0,r):
