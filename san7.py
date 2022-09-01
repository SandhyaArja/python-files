import calendar
year=int(input())
month=int(input())
date=int(input())
leapyear=True
count=0
while leapyear:
        if year%400==0 or (year%4==0 and year%100!=0):
            print(year,"is leapyear")
            leapyear=False
            count+=1
            day=calendar.weekday(year,month,date)
            if day==6 or day==7:
                print(date,"its a holiday")
                print(calendar.month(year,month))
            else:
                print(date,"its a week day")
                print(calendar.month(year,month))
        else:
            if count==0:
                print(year,"Not a leap year")
            count+=1
            year+=1
