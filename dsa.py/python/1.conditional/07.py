order_size = str(input("Amount of size order: "))
extra_shot = bool(input("is it extra shot? "))

if extra_shot == True:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + "coffee"

print("Order: ", coffee)
