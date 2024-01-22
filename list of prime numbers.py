n=int(input("enter number: "))
sum=0
prime=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            sum=sum+1
    if sum==0:
        prime.append(i)
    else:
        sum=0
print(prime)