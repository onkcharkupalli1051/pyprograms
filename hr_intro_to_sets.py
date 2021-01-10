
import calendar

k = map(int, input().split())
n = calendar.weekday(k[2],k[0],k[1])

if(n == 0)
    print("Monday")
elif(n == 1)
    print("Tuesday")
elif(n == 2)
    print("Wednesday")
elif(n == 3)
    print("Thursday")
elif(n == 4)
    print("Friday")
elif(n ==  5)
    print("Saturday")
elif(n == 6)
    print("Sunday")
 



