
n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

n1_f = []
for i in range(1,n1+1):
    if n1%i == 0:
        n1_f.append(i)

n2_f = []
for j in range(1,n2+1):
    if n2%j == 0:
        n2_f.append(j)

cf = []
for i in n1_f:
    for j in n2_f:
        if i==j:
            cf.append(i)

print(n1_f,n2_f,cf)
print("GCD : {}".format(cf[-1]))