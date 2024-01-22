import random
n=int(input("Enter your range: "))
S=[]
R=[]
N=[]
for i in range(1,n+1):
    l=int(input(f"Element no.{i} : "))
    S.append(l)
    R.append(l)
print(S)
S.sort()
print(S)
S.sort(reverse=True)
print(S)
print(min(S))
print(max(S))
print(sum(S))
R.reverse()
print(R)
