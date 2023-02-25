#find the day of a date
date=input("Enter the date (year,month,date): ")

given_date=date.strip().split(",")
year=int(given_date[0])
month=int(given_date[1])
date=int(given_date[2])


if month<3:
    month=month+12
    year=year-1
a=2*month+6*(month+1)//10
b=year+year//4-year//100+year//400
f1=date+a+b+1
f=f1%7

if f==0:
    print("Sunday")
elif f==1:
    print("Monday")
elif f==2:
    print("Tuesday")
elif f==3:
    print("Wednesday")
elif f==4:
    print("Thursday")
elif f==5:
    print("Friday")
else:
    print("Saturday")
    
    
