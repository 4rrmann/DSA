pet = str(input("is it dog or cat?\n :"))
years = int(input("drop age: "))

if pet == "dog":
    if years<2:
        print("Puppy food seems best choice")
    else:
        print("here's your dog food")
elif pet == "cat":
    if years>5:
        print("Ah! here's your Senior cat food")
    else:
        print("here's your cat food")
else:
    print("Sorry we have only cat or dog foods only")