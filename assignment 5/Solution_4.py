a=int(input("Enter the number of rows:"))
i=0
for i in range (0,a):
    for j in range (0,i+1):
        print("* ", end="")
    print("\r")
for i in range (a,0,-1):
    for j in range (i+1,0,-1):
        print("* ", end="")
    print("\r")
