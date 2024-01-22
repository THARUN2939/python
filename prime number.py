a=int(input("Enter a number: "))
sum=0
for i in range(2,a):
    if a%i==0:
        sum=sum+1
    i=i+1
if sum==0:
    print("Prime Number")
else:
    print("Not Prime Number")