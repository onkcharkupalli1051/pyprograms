"""
Write a Python function intersect(l1,l2) that takes two sorted lists as arguments and returns the list of all elements common to both l1 and l2 in the same order that they appear in the two lists. If the same element occurs more than once in both lists, it should appear in the output exactly once.

Thus, intersect([2,2,4],[1,2,2,3,4]) should return [2, 4] while intersect([1,2,3],[4,5,6]) should return [].
"""

def intersect(l1,l2):
    l = []
    for ele in l1:
        if ele in l2:
            if ele not in l:
                l.append(ele)
    return(l)

print(intersect([1,2,3],[4,5,6]))