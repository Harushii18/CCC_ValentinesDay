import math

x=int(input())
y=int(input())

if ((x-15)%60==0):
    count=x
    while (count<=y):
        print("All positions change in the year",count)
        count+=60
else:
    if (x>15):
        num=math.ceil(x/60)
    else:
        num=math.floor(x/60)
    count=60*(num)+15
    
    while (count<=y and count>=x):
        print("All positions change in the year",count)
        count+=60
    