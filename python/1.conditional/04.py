fruit = "Banana"
appearance = str(input("enetr the appearance of the fruit: "))

if fruit == "Banana":
    if appearance == "green":
        print("Unripe")
    elif appearance == "yellow":
        print("Ripe")
    elif appearance == "brown":
        print("Overripe")
    else:
        print("Please validate your input!")