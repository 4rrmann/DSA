chr = str(input("Character: ")) #yyyooehhc

for i in chr:
    print(i)
    if chr.count(i) == 1:
        print(" The non-repeating chr:", i)
        break