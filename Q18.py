import math

sums=[]
m=int(input())
n=int(input())

count=0;
for i in range(1,m):
    diff=abs(i-10);
    if (i+diff<=10):
        strThing=i,"+",diff,"=10"
        if (diff<=n and diff>0):
            sums.append(strThing)
            # print(strThing)
            count+=1;
            
for j in range(1,n):
    diff=abs(j-10);
    if (j+diff<=10):    
        strThing=diff,"+",j,"=10";
        if (diff<=m and diff>0):
            if (not strThing in sums):
                sums.append(strThing)
                # print(strThing)
                count+=1;
        
if (count==1):
    print("There is",count,"way to get the sum 10")
else:
    print("There are",count,"ways to get the sum 10")

    

    
        



