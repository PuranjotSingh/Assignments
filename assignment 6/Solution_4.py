import string
 
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True
     
string =input("Input the string to be analyzed") 
if(ispangram(string) == True):
    print("Yes, the input string is a pangram")
else:
    print("No,the input string is not a pangram")