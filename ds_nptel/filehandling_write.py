fh = open("new.txt","w")

fh.write("This is new line\n")
fh.write("this is second line\n")
l = "hi how are you"
fh.writelines(l)
fh.close()

fh = open("new.txt","r")
for i in fh.readlines():
    i = i.rstrip()
    print(i)

fh.flush()