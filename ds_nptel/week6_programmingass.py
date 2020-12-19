i = input()
li = list(i.split())
nli = []
string = ""
for ele in li:
    ele = int(ele)
    if ele in nli:
        None
    if ele not in nli:
        nli.append(ele)

for ele in nli:
    string = string + str(ele) + " "

print(string,end=" ")
