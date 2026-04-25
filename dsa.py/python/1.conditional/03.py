marks = int(input("enter marks: "))

if marks>100:
    print("Invalid input!")
    exit()

if marks<60:
    print("F")
elif marks<70:
    print("D")
elif marks<80:
    print("C")
elif marks<90:
    print("B")
else:
    print("A")