"""
Question 3
Here is a function to compute the largest of four input integers. You have to fill in the missing lines.

def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line


  # Your code above this line
  return(maximum)
Open up the code submission box below and fill in the gap in the code. Ensure that you maintain correct indentation.

def max4(w,x,y,z):
    if (w >= x) and (w >= y) and (w >= z):
        maximum = w
  # Your code below this line
    elif (x >= w) and (x >= y) and (x >= z):
        maximum = x
    elif (y >= w) and (y >= x) and (y >= z):
        maximum = y
    else:
        maximum = z
  # Your code above this line
    li = [w,x,y,z]
    li.sort()
    print(li)
    return(maximum)
"""

def max4(w,x,y,z):
    max = 0
    if (w>=x) and (w>=y) and (w>=z):
        max = w
    elif (x >= w) and (x >= y) and (x >= z):
        max = x
    elif (y >= x) and (y >= w) and (y >= z):
        max =y
    else:
        max = z
    return max

print(max4(4,1,3,2))