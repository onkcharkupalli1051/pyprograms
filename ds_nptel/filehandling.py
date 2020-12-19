#open a file for reading file
fh = open("fd.txt","r")

#create an empty file to write to
#fh = open("fd.txt","w")

#append to an existing file
#fh = open("fd.txt","a")

#reads entire file into name as a single string
#contents = fh.read()

#reads one line into name-lines end with '\n'
#contents_one_line = fh.readline()

#reads entire file as a list of strings
nc = fh.readlines()

#print("All string : \n",contents)

#print("\nlines with \\n : ",contents_one_line)
for i in nc:
    print(i)

