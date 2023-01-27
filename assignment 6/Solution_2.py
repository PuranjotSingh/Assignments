a=input("Enter the word or string to be analyzed: ")
a=a.replace(" ","")
rev=a[::-1]
if rev==a:
    print("The given statement is a palindrome")
else:
    print("The given statement is not a palindrome")