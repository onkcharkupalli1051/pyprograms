#1
"""def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])

a = mystery([22,14,19,65,82,55])
print(a)"""

#2
"""pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
print(pairs)
"""

#3
"""
wickets = {"Tests":{"Kumble":[3,5,2,3],"Srinath":[4,4,1,0],"Prasad":[2,1,7,4]},"ODI":{"Kumble":[2,0],"Srinath":[1,2]}}
wickets["ODI"]["Prasad"] = [4,4]
print(wickets)

in the above program, which of the below code does not give erroe
 wickets["ODI"]["Prasad"][0:] = [4,4]
 wickets["ODI"]["Prasad"].extend([4,4])
 wickets["ODI"]["Prasad"] = [4,4]        == ans
 wickets["ODI"]["Prasad"] = wickets["ODI"]["Prasad"] + [4,4]
"""
#4
hundreds = {}
hundreds[["Tendulkar", "international"]] = 100 #this gives an errror... which is ans. of question
