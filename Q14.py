#get minutes
daytime=int(input())
evening=int(input())
weekend=int(input())

aCost=0;
bCost=0;
#daytime calcs
if (daytime>100):
    aCost=(daytime-100)*25;
if (daytime>250):
    bCost=(daytime-250)*45;

#evening calcs
aCost+=(evening*15)
bCost+=(evening*35)

#weekend calcs
aCost+=(weekend*20)
bCost+=(weekend*25)

aCost=aCost/100
bCost=bCost/100
print("Plan A costs","{:.2f}".format(aCost))
print("Plan B costs","{:.2f}".format(bCost))

if (aCost>bCost):
    print("Plan B is cheapest.")
elif (aCost<bCost):
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")


    

    