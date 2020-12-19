def mystery(l):
    if l == []:
        return(l)
    else:
        print(l[1:] + l[:1])
        print()
        return(mystery(l[1:])+l[:1])

print(mystery([22,14,19,65,82,55]))
