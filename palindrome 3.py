n=int(input("enter number: "))
S=str(n)
N=S[::-1]
if N==S:
    print("Palindrome")
else:
    print("NOT Palindrome")