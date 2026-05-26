age = int(input("enter age: "))

if age<13:
    print("Child")
if age<20:
    print("Teenager")
elif age<60:
    print("Adult")
    
else:
    print("Senior")