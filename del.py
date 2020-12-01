def subsequence(l1, l2):
    flag = False
    l1 = list(l1)
    l2 = list(l2)
    for i in range(0, len(l2)):
        if (l1 == l2[i:i + len(l1)]):
            flag = True
    return flag

print(subsequence([2,2,5],[2,2,3,4,5]))