x=int(input("Enter the year to be analyzed--"))
if x%4==0:
    leap_year=True
if x%100==0:
    if x%400==0:
        leap_year=True
    else :
        leap_year=False
if leap_year:
    print("The given year is a leap year")
else: 
    print("The given year is not a leap year")