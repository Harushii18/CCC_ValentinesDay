
#get input
x=int(input());
m=int(input());

if (x%2==0 and m%2==0):
    print("No such integer exists.")
else:
    nums=[x,m]
    small=min(nums)
    #get gcd
    for i in range(2,small+1):
        if (x%i==m%i):
            print("No such integer exists.")
            quit();
    #gcd is 1 from here
    
    #can calculate mod inverse
    print( pow(x, -1, m))
    