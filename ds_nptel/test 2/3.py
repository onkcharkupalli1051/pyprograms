"""
Question 3
Here is a function to compute the third smallest value in a list of distinct integers. All the integers are guaranteed to be below 1000000. You have to fill in the missing lines. You can assume that there are at least three numbers in the list.

def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
  # Your code below this line


  # Your code above this line
  return(mythirdmin)
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.
"""
def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
    # Your code below this line
    pass
  l = [4,1,3,2]
  l = sorted(l, reverse )
  print(l[2])