n=input("Enter a number: ")
a=len(n)
n=int(n)
m=int(n)
S=0
while n>0:
    b=n%10
    n=int(n/10)
    S+=(b**a)
if S==m:
    print(m,"is Armstrong Number.")
else:
    print(m,"is not Armstrong Number.")