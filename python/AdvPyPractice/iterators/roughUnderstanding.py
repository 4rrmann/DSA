channels = ['CN', 'DisneyXD', 'PoGO', 'Nickelodeon']
for i in channels:
    print(i)
    pass

itr = iter(channels)
print("\n", itr, "\n")

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr)) #raising StopIteration exception

print("\n", dir(itr), "\n") #methods

#Reverse Iterator:
itr = reversed(channels)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))