#QUESTION 1: GENERATED CALENDAR

class color:
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#array to store the days of the week
DaysOfWeek=["Sun","Mon","Tues","Wed","Thurs","Fri","Sat"];

#get the input
startDay=int(input()); #day of week that month starts on
numDays=int(input()); #num days in month

for i in range(0,len(DaysOfWeek)):
    print(DaysOfWeek[i], end ="");
    #ensure there isn't a tab at the end
    if (i<len(DaysOfWeek)-1):
        print("\t", end ="");
    
print("\n", end ="")
#stores number of days
count=1;
#only output first week 
for i in range(0,7):
    if (i<startDay-1):
        print("\t", end =" ");
    else:
        print(count, end ="");
        if (i!=6):
            print("\t", end ="");
        count+=1;
print("\n", end ="")
weekCounter=0;
while (count<=numDays):
    #if it is valentine's day
    if (count==14 and (numDays==28 or numDays==29)):
        print(color.RED + str(count) + color.END,end ="")
    else:
        print(count, end ="");
    count+=1;
    if (weekCounter!=6):
        print("\t", end ="");
        
    weekCounter+=1;
    #ensures new weeks are printed on new lines
    if (weekCounter==7):
        weekCounter=0;
        print("\n",end="");
    

    

