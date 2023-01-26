
a=int(input("Enter the lower bound of the range:"))
b=int(input("Enter the upper bound for the range:"))

for number in range(a,b+1):
    if number>1:
        for i in range (2,number):
            if number%i==0:
                break
        else:
            print(number)
