N=int(input())
stringTxt=""
for i in range(N):
    stringTxt+=input()
tCount=stringTxt.count('t')+stringTxt.count('T')
sCount=stringTxt.count('s')+stringTxt.count('S')

if (tCount>sCount):
    print('English')
else:
    print('French')
    
    