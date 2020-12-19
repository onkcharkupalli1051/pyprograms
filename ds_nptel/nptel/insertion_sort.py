def inss(l):
    for _ in range(len(l)):
        for i in l:
            j = l.index(i)+1
            if j < len(l):
                print(i,l[j])
                if i > l[j]:
                    temp = i
                    i = l[j]
                    l[j] = temp
                    print(i,l[j])
                    print("\n")
            else:
                pass

    return l

print(inss([98,65,48,99,22,45]))

