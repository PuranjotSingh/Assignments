
i=0
list_1=[]
while i<10:
    a=int((input("Enter a number:")))
    list_1.append(a)
    i+=1


print("Question A----")
for i in list_1:
    if i<0:
        continue
    if i>0:
        print(i,end=" , ")
print("These are Positive numbers in the input numbers")
print("\r")

  
print("Question B----")
for i in list_1:
    if i>0:
        continue
    if i<0:
        print(i,end=" , ")
print("These are Negative numbers in the input numbers")
print("\r")

list_even=[]
list_odd=[]
for i in list_1:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print("Question C----")
print("Odd numbers in the input numbers are",list_odd)
print("\r")
print("Question D----")
print("Even numbers in the input numbers are",list_even)
print("\r")
print("Question E----")
dic_1={}
for i in list_1:
    dic_1.update({i:list_1.count(i)})
print("The number of occurances of any number are",dic_1)