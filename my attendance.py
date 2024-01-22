n=int(input("No. of classes held = "))
l=int(input("No. of classes attended = "))
if l>n:
    print("Wrong values entered.")
else:
    p=(round(l/n,4))*100
    print(f"Attendance = {p}%")
    if p>=75:
        print("ALLOWED")
    else:
        m=int(input("Medical Proof available?(type 1 for YES and 0 for NO) "))
        if m!=0 and m!=1:
            print("Wrong values entered.")
        elif m==1:
            print("ALLOWED")
        else:
            print("NOT ALLOWED")
