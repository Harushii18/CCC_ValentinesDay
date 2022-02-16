def calculateNums(x,y):
    totCount=0;
    for i in range(x,y):
        count=0;
        for j in range(1,i+1):
            if (i%j==0):
                count+=1;
                if (count==4):
                    totCount+=1;
                    break;
    return totCount;
            
x=int(input())
y=int(input())
if (x>y):
    totCount=calculateNums(y,x);
    print("The number of RSA numbers between",y,"and",x,"are", totCount)
else:
    totCount=calculateNums(x,y);
    print("The number of RSA numbers between",x,"and",y,"are", totCount)

