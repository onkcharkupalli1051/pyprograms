"""
Question 1
Here is an function to return the maximum value among three positive integers. There is an error in this function. Provide an input triple (n1,n2,n3), where n1, n2 and n3 are all positive integers, for which max3bad produces an incorrect output.

def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)
Open up the code submission box below and write your test case where you would normally paste your code. Your input should be in the form of triple (n1,n2,n3), where n1, n2 and n3 are all positive integers.
"""
def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)

print(max3bad(9,-100,23))
