from math import sqrt
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
#checking the validity of the triangle 
if a<=b+c and b<=a+c and c<=a+b:
    print("Triangle is possible")
else:
    print("The Triangle is not possible")
    exit()
#finding semiparameter
s=(a+b+c)/2
# finding the area of the triangle using herons formula 
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle by using herons formula is",area)