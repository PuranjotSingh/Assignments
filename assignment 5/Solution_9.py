a=input("Input the string:")

dict_1= dict()
Split_txt = str.split(a)

for t in Split_txt:
	if t in dict_1:
		dict_1[t] += 1
	else:
		dict_1[t] = 1

print(dict_1)