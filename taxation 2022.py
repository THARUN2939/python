n=int(input("Enter your Annual Income: "))
if 0<=n<=250000:
    print("Income Tax to be paid = 0")
elif 250000<n<=500000:
    a=n-250000
    b=a*0.05
    print("Income Tax to be paid =",b)
elif 500000<n<=750000:
    a=n-500000
    b=12500+(a*0.1)
    print("Income Tax to be paid =",b)
elif 750000<n<=1000000:
    a=n-750000
    b=37500+(a*0.15)
    print("Income Tax to be paid =",b)
elif 1000000<n<=1250000:
    a=n-1000000
    b=75000+(a*0.2)
    print("Income Tax to be paid =",b)
elif 1250000<n<=1500000:
    a=n-1250000
    b=125000+(a*0.25)
    print("Income Tax to be paid =",b)
else:
    a=n-1500000
    b=187500+(a*0.3)
    print("Income Tax to be paid =",b)