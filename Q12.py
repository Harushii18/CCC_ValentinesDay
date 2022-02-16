keyword=input()
strEnc=input()
strLen=len(strEnc)
newStr=""
#remove non alphabetic characters
for i in strEnc:
    if (i.isalpha()==True):
        newStr+=i
strEnc=newStr

keyLen=len(keyword)

count=0
ans=""
for j in range(0,len(strEnc)):
    if (count==keyLen):
        count=0
    for i in range(0,keyLen):
        if (i==count):
            # add two letters together
            num=ord(strEnc[j])+(ord(keyword[i])-65)
            # print(strEnc[i],ord(strEnc[j]),keyword[i],(ord(keyword[i])-65))
            
            #ensure letters wrap around
            while (num>90):
                num=num-26
            ns=chr(num)
            print(ns,end="")
            # print(ns, ord(ns))
    count+=1 

            