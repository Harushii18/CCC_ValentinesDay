def swap(i,j):
    tmp=i;
    i=j;
    j=tmp; 
    return i,j

allIn=input()
thing=allIn.split(" ")
#separate n and x from input
N=int(thing[0])
X=int(thing[1])

num=input()
nums=num.split(' ')
lNums=[]
for i in nums:
    lNums.append(int(i))

count=0
for l in range(N-2):
    for m in range(l+1,N-1):
        for o in range(m+1,N):  
            i=lNums[l];
            j=lNums[m]
            k=lNums[o]
                
            if (i>j):
                i,j=swap(i,j)
            if (i>k):
                i,k=swap(i,k)
            if (k<j):
                k,j=swap(k,j)
            
            if ((j+k+i)/3==X):
                if (j==X):
                    # print("Triples:","i:",i,",j:",j,",k:",k)
                    count+=1    
print(count)
        
    
        
    

