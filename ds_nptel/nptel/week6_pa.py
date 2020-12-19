course_data = []

stu = {}

while(1):
    c = list(input().split("\n"))
    if c[0] == 'Courses':
        for ele in c[1:]:
            pass

    elif c[0] == "Students":
        for ele in c[1:]:
            ele = list(ele.split("~"))
            if ele[0] not in stu.keys():
                stu[ele[0]] = ele[1]

    elif c[0] == "Grades":
        for ele in c[1:]:
            ele = list(ele.split("~"))




