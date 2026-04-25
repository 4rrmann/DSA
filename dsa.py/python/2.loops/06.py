num = int(input("enter the number: "))

factorial = 1
while(num>0):
    factorial *= num
    num -=1

print(" Factorial: ", factorial)