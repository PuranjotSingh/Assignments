a=int(input("Enter the lower bound of the range:"))
b=int(input("Enter the upper bound of the range:"))
c=int(input("Enter the number to divisible with:"))
for i in range (a,b):
    if i%c==0:
        if i!=0:   #creating a fail safe for zero
            print(i, end=" ")
        else:
            continue

        