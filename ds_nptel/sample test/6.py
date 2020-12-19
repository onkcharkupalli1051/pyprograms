"""
Question 6
Write a Python function sublist(l1,l2) that takes
two sorted lists as arguments and returns True if
the the first list is a sublist of the second list,
and returns False otherwise.

A sublist of a list is a segment consisting of
contiguous values, without a gap. Thus, [2,3,4] is a
 sublist of [2,2,3,4,5], but [2,2,4] and [2,4,5] are
  not.
"""

def sublist(l1,l2):
    i = l2.index(l1[0])
    print(l1)
    print(l2[i:len(l1)])
    if l1[0:len(l1)] == l2[i:len(l1)]:
        return True
    return False

print(sublist([2,2,4],[2,2,3,4,5]))