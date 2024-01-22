n=int(input("Enter a number:"))
P=1
if n<0:
    print("factorial does not exist.")
elif n==0:
    print(1)
else:
    for i in range(n):
        P=P*(n-i)
    print(P)