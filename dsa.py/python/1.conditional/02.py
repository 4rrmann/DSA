age = int(input("enter age: "))
day = str(input("enter the day of week: "))

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print(f"Ticket price for you is ${price}")
