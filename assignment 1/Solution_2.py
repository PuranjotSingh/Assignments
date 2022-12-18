a=int(input("Enter your Annual Income: "))
b=int(input("Enter number of dependents: "))
taxable_income=a-10000-(3000*b)
tax=taxable_income*20/100
print("Total tax is Rs.",tax,"/-")
