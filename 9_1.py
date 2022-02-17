from math import gcd as bltin_gcd
def coprime2(a, b):
    return bltin_gcd(a, b) == 1

#get single line input
All=input()
#split by space
ans=All.split()
A=int(ans[0])
B=int(ans[1])
C=int(ans[2])
D=int(ans[3])

count=0
# check co primes
for i in range(A,B+1):
    for j in range(C,D+1):
        if (coprime2(i,j)):
            count+=1 
print(count)
            
    