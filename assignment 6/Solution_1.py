a= int(input("Enter the number to be analysed:"))
b=0
for i in range (1,a):
    if a%i==0:#checking if divisor
        b=b+i

#checking if the number is perfect or not
if b==a:
    print("The number is perfect")
else:
    print("The number is not perfect")