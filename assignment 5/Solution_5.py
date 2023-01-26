#we will procede with the ascii approach
#as we know ascii of A is 65 and ascii of Z in 90
ascii_no=65
a=int(input("Enter the number of rows:"))
for i in range (0,a):
    for j in range(0,i+1):
        print(chr(ascii_no),end="")
        if ascii_no<90:
            ascii_no +=1
        else:
            ascii_no=65
    print("\r")