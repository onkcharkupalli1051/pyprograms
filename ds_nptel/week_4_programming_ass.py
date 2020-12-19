'''
def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    return (min_freq_list, max_freq_list)
'''
"""
def onehop(l):
    li = []
    tup = ()
    i = 0

    for a in l[i]:
        for b in l[i+1]:
            for element in a not in b:
                tup.append(element)
            for element in b not in a:
                tup.append(element)
        li.append(tup)
        i += 1

    return li
"""
def onehop(lis):
    er=[]
    for (i,j) in lis:
        for (k,l) in lis:
            if (i!=k and j!=l)and(i==l or j==k) and (((i,j) not in er) and ((k,l) not in er)):
                m=lis.pop(lis.index((i,j)))
                n=lis.pop(lis.index((k,l)))
                er.extend([m,n])
    for i in range(len(er)):
        if er[i][0]>er[i][1]:
            er[i]=(er[i][1],er[i][0])
    ans=sorted(er,key=lambda item: (item[0],item[1]))
    return ans
print(onehop([(1,2),(3,4),(5,6)]))