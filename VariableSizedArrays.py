n,q = map(int, input().split())

a = []
p = []

for i in range(n):
    l = list(map(int, input().split()))
    k = l[0]
    l.pop(0)
    a.append(l)

for m in range(q):
    i,j = map(int, input().split())
    p.append(a[i][j])

for ele in p:
    print(ele)


