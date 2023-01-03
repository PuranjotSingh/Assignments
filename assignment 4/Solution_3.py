import random

i=0
while i<10:
    i=i+1    
    x=random.randint(1,10)
    y=random.randint(1,10)
    z=x*y
    print("Multiply-            ",x,"x",y)
    answer=int(input("Input your answer--"))
    if answer==z:
        print("Your answer is correct")
    else:
        print("your answer is incorrect, The correct answer is",z)
