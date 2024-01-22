n=int(input("enter number: "))
S=str(n)
N=list(S)
sum=0
if len(N)==1:
    print(f"{n} is palindrome number.")
else:
    for i in range(len(N)):
        if N[i]==N[len(N)-1-i]:
            sum=sum+1
        else:
            continue
    if sum==len(N):
        print(f"{n} is palindrome number.")
    else:
        print(f"{n} is NOT palindrome number.")