#Python Program to check leap year

yr=int(input("enter year"))
if yr%100==0 and yr%400==0:
    print(yr,"is a leap year")
elif yr%4==0:
    print(yr,"is a leap year")
else:
     print(yr,"is not a leap year")
