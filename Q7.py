import math

t=int(input())
s=int(input())
h=int(input())

width=s*2+3

#for tines
for j in range(0, t):
    line=""
    for i in range(0,width):
        if (i==0 or i==s+1 or i==width-1):
            line+="*"
        else:
            line+=" "
    print(line)
#middle part of trident
line=""
for i in range(0, width):
    line+="*"
print(line)

#get pos of where handle should be
median=math.ceil(width/2)
for i in range(0,h):
    line=""
    for j in range(0, width):
        if (j==median-1):
            line+="*"
        else:
            line+=" "
    print(line)



        