a=int(input("Enter the length of First side of the triangle: "))
b=int(input("Enter the length of the Second side of the triangle: "))
c=int(input("Enter the length of Third side of the triangle: "))

if a>=b+c :
    print("NO")
if b>=a+c :
    print("NO")
if c>=a+b :
    print("NO")
else :
    print("YES")
