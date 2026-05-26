distance = int(input("enetr the distance(km): "))

if distance<3:
    mode = "Walk"
elif distance<15:
    mode = "Bike"
else:
    mode = "Car"

print(f"Choose: {mode}")