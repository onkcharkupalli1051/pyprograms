com = list(input().split("+"))

x = int(com[0])
y = list(com[-1])
y.remove("j")
y = int("".join(y))
print(x)
print(y)