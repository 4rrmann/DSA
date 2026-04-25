def even_generator(limit):

    for i in range(2, limit+1, 2):
        yield i #return the value & also stores in memory (func as well as their state)

lim = int(input("Range limit: "))
for i in even_generator(lim):
    print(i)