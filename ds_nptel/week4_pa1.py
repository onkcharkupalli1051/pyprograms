def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)

"""    min = []
    max = []
    dic = {}

    for ele in l:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] += 1
    print(dic)
    for
    min = list(sorted(dic.keys()))
    max = list(sorted(dic.keys(), reverse=True))
    return (min,max)"""

print(frequency([13,12,11,13,14,13,7,11,13,14,12]))


