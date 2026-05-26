number = int(input("Number: "))
print(f"Multiplication of {number}:")

for i in range(1, 11):
    if i==5:
        continue #pass
    print(i*number)