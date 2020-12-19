"""
Question 6
Write a Python function subsequence(l1,l2) that takes two sorted lists as arguments and returns True if the the first list is a subsequence of the second list, and returns False otherwise.

A subsequence of a list is obtained by dropping some values. Thus, [2,3,4] and [2,2,5] are subsequences of [2,2,3,4,5], but [2,4,4] and [2,4,3] are not.
"""
def subsequence(l1, l2):
  count = 0
  for i in l1:
    if i in l2:
      l2.remove(i)
      count += 1
  if count == len(l1):
    return(True)
  else:
    return(False)
