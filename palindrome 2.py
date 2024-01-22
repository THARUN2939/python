def rev(list):
    rev_list=[]
    for i in range(len(list)):
        rev_list.append(list[len(list)-1-i])
    return rev_list
n=int(input("enter number: "))
S=str(n)
N=list(S)
if rev(N)==N:
    print(f"{n} is Palindrome Number.")
else:
    print(f"{n} is NOT Palindrome Number.")