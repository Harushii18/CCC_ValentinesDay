import math

#get height h
h=int(input());

#check if h is off and greater than or equal to 5
if ((h>=5) and (h%2!=0)):
    #2n-1 is the bowtie formula
    
    #gets median for middle full portion
    median=math.ceil(h/2)

    for i in range(1,median):
        outStr="";
         #sets it at length h*2
        for x in range(0,h*2):
            outStr+=" "
    
        listStr=list(outStr);
        count=0;
        count2=h*2-1;
        for j in range(1, (2*i)):
            listStr[count]='*';
            count+=1;
            listStr[count2]='*';
            count2-=1;
        outStr = ''.join(listStr);
        print(outStr);
    
    #prints middle portion of bowtie
    for i in range(h*2):
        print("*",end="")
    print()
    
    #prints end portion of bowtie
    for i in range(median-1,0,-1):
        outStr="";
         #sets it at length h*2
        for x in range(0,h*2):
            outStr+=" "
    
        listStr=list(outStr);
        count=0;
        count2=h*2-1;
        for j in range(1, (2*i)):
            listStr[count]='*';
            count+=1;
            listStr[count2]='*';
            count2-=1;
        outStr = ''.join(listStr);
        print(outStr);
else:
    print("Invalid");
    