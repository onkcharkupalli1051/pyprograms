"""
Question 4
A list is a palindrome if it reads the same forwards
 and backwards. For instance [], [7], [8,11,8] and
[19,3,44,44,3,19] are palindromes, while [3,18,4]
and [23,14,3,14,3,23] are not. Here is a recursive
function to check if a list is a palindrome. You
have to fill in the missing argument for the
recursive call.

def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(...)
Open up the code submission box below and fill
in the missing argument for the recursive call.

"""
def mypalindrome(l):
    if l == [] or len(l) == 1:
        return True
    elif (len(l) > 1):
        nl = l[::-1]
        if nl == l:
            return True
        else:
            return False
        
print(mypalindrome([12,22,12,22]))


