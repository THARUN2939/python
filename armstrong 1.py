n=input("Enter a number:")
a=len(n)
d=len(n)
n=int(n)
m=int(n)
S=0
while n>0:
    b=10**(a-1)
    c=int(n/b)
    n=n%b
    a=a-1
    S=S+(c**d)
if S==m:
    print(m,"is Armstrong Number")
else:
    print(m,"is not Armstrong Number")


    
