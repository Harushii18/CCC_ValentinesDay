class outputMaker:
    digitStr="";
#I REALISED THIS CLASS WAS COMPLETELY UNNECESSARY
#COULD HAVE USED JUST A STRING VAR

def makeZero():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n     ";
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    return d;

def makeOne():
    d=outputMaker();
    d.digitStr="     "
    for i in range(0,3):
        d.digitStr+="\n*    ";
    d.digitStr+="\n     ";
    for i in range(0,3):
        d.digitStr+="\n*    ";
    d.digitStr+="\n     ";
    return d;

def makeTwo():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n*    ";
    d.digitStr+="\n *** ";
    return d;

def makeThree():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n *** ";
    return d;

def makeFour():
    d=outputMaker();
    d.digitStr="     "
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n     ";
    return d;

def makeFive():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n*    ";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n *** ";
    return d;

def makeSix():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n*    ";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    return d;

def makeSeven():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n     ";
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n     ";
    return d;
    
def makeEight():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    return d;

def makeNine():
    d=outputMaker();
    d.digitStr=" *** "
    for i in range(0,3):
        d.digitStr+="\n*   *";
    d.digitStr+="\n *** ";
    for i in range(0,3):
        d.digitStr+="\n    *";
    d.digitStr+="\n *** ";
    return d;
    
    
    
digits=["0","1","2","3","4","5","6","7","8","9"]
number=input();
#Add all numbers to the class
d0=makeZero();
d1=makeOne();
d2=makeTwo();
d3=makeThree();
d4=makeFour();
d5=makeFive();
d6=makeSix();
d7=makeSeven();
d8=makeEight();
d9=makeNine();


#just to test my numbers are correct in look-> can paste
#later for doc if needed

# print(d0.digitStr);
# print(d1.digitStr);
# print(d2.digitStr);
# print(d3.digitStr);
# print(d4.digitStr);
# print(d5.digitStr);
# print(d6.digitStr);
# print(d7.digitStr);
# print(d8.digitStr);
# print(d9.digitStr);

for i in range(0, len(number)):
    if (number[i]=="0"):
        print(d0.digitStr);
    elif (number[i]=="1"):
        print(d1.digitStr);
    elif (number[i]=="2"):
        print(d2.digitStr);
    elif (number[i]=="3"):
        print(d3.digitStr);
    elif (number[i]=="4"):
        print(d4.digitStr);
    elif (number[i]=="5"):
        print(d5.digitStr);
    elif number[i]=="6":
        print(d6.digitStr);
    elif (number[i]=="7"):
        print(d7.digitStr);
    elif (number[i]=="8"):
        print(d8.digitStr);
    elif (number[i]=="9"):
        print(d9.digitStr);
    



