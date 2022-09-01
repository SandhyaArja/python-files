#leapyear
def findtheleapyear():
    if(year%4==0 and year%100==0):
        print(year,"given year is leapyear")
    elif (year%400==0):
        print(year,"given year is a leapeyear")
    else:
        for i in range(year+1,year+4):
            if(i%4==0 and i%100==0):
                print(i,"neat year")
                break
            elif (i%400==0):
                print(i,"year is next year")
                break

year =int(input())
findtheleapyear()

#check the given year is leapyear or not
year=int(input())
if year%4==0 and year%400:
    print("Leapyear")
elif year%100==0 or year%400!=0:
    print("It's not a leapyear")

#task there extenion
import calendar
year=int(input())
month=int(input())
date=int(input())
leapyear=True
count=0
while leapyear:
    if year%4==0 and year%400==0:
        print(year,"is leapyear")
        leapyear=False
        count+=1
        calendar.weekday(year,month,date)
        if day==6 or day==7:
            print(date,"its a holiday")
            print(calendar.calendar(month))
        else:
            print(date,"its a week day")
            print(calender.calender(month))
    else:
        if count<=0:
            print(year,Not a leap year)
            count+=1
            year+=1
