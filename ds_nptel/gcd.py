n1 = int(input("Enter 1st no. : "))
n2 = int(input("Enter 2nd no. : "))

if n1<n2:
    low = n1
else:
    low = n2
print(low)

div_list = list(range(1,low+1))
print(div_list)

largest = div_list[0]
print(largest)

for i in div_list:
    if n1%i == 0 and n2%i == 0 and i > largest:
        largest = i

print("GCD : {}".format(largest))