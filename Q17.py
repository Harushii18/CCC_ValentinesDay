lstIn=[]
inst=input()
while (inst!="SCHOOL"):
    lstIn.append(inst);
    inst=input();
for i in range(len(lstIn)-1,-1,-1):
    if (i!=0):
        if (lstIn[i]=="R"):
            print("Turn LEFT onto",lstIn[i-1],"street")
        elif lstIn[i]=="L":
            print("Turn RIGHT onto",lstIn[i-1],"street")
    else:
        if (lstIn[i]=="R"):
            print("Turn LEFT into your HOME")
        else:
            print("Turn RIGHT into your HOME")
    