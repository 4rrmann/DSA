def greet(name):
    return " Oh! wlcm " +name

yourname = str(input("yourname: "))
print(greet(yourname or "X"))