"""
Write a Python function repeated(l) that takes a list of immutable values as argument. The function should return the number of values that are repeated in the input list.

For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated. Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values, "the" and "you", are repeated.

Sample Test Cases
Input	Output
Test Case 1
repeated([1,17,22,17,23,17])
1
Test Case 2
repeated(["the","higher","you","climb","the","further","you","fall"])
2
Test Case 3
repeated([13,12,13,12,13,12,23,23,14,15,15,14])
5
Test Case 4
repeated([1,2,3,4,5])
0
Test Case 5
repeated([1,17,22,17,23,17])
1
Test Case 6
repeated(["the","higher","you","climb","the","further","you","fall"])
2

The due date for submitting this assignment has passed.
"""

def repeated(l):
    dic = {}
    for ele in l:
        if ele not in dic.keys():
            dic[ele] = 1
        elif ele in dic.keys():
            dic[ele] += 1
    count = 0
    for val in dic.values():
        if val >= 2:
            count += 1
    return count

print(repeated([1,2,3,4,5]))