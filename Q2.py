#stores the digits that can be rotated
rotDigits=["0","1","6","8","9"];
#stores the digits that can't be rotated
nonRotDigits=["2","3","4","5","7"]

m=int(input());
n=int(input());

#stores num rotatables
count=0;
for i in range(m,n+1):
    num=str(i);
    valid=True;
    rotNum="";
    #loop through number
    for j in range(0,len(num)):
        if (num[j] in nonRotDigits):
            valid=False;
            #don't check the num anymore
            break;
        else:
            if (num[j]=="6"):
                rotNum+="9";
            elif (num[j]=="9"):
                rotNum+="6";
            else:
                rotNum+=num[j];
    #reverse the rotated number
    rotNum=''.join(reversed(rotNum))
    if (rotNum!=num):
        valid=False;
    if (valid==True):
        # output for just testing if am correct
        # print(num);
        count+=1;
print(count);
    