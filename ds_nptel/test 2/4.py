"""
Question 4
Recall that the positions in a list of length n are 0,1,…,n-1. We want to write a function oddpositions(l) that returns the elements at the odd positions in l. In other words, the function should return the list [l[1],l[3],...]. For instance oddpositions([]) == [], oddpositions([7]) == [], oddpositions([8,11,8]) == [11] and oddpositions([19,3,44,44,3,19]) == [3,44,19]. A recursive definition of oddpositions is given below. You have to fill in the missing argument for the recursive call.

def oddpositions(l):
  if len(l) <= 1:
    return([])
  else:
    return(...)
Open up the code submission box below and fill in the missing argument for the recursive call.
"""

def oddpositions(l):
  if len(l) <= 1:
    return([])
  else:
      return l[1] + oddpositions(l[2:])

print(oddpositions([8, 11, 8]))
