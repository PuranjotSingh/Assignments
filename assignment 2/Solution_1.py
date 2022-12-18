x= "Python is a case sensitive language"

# a)using len() to find the length
print(len(x))


# b)using slicing to reverse the order of strings
txt=x[::-1]
print(txt)


# c) Using slicing
s=slice(10,26)
New_string=x[s]
print(New_string)


# d) Using Replace()
a=x.replace("a case sensitive", "object oriented")
print(a)


# e) Using index()
print(x.index("a"))


# f) Using Replace()
print(x.replace(" ",""))
