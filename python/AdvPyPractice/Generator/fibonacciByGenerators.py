#Produce fibonacci sequence using generator
def fibo():
    a, b = 0, 1 #base-case
    while True:
        yield a
        a, b = b, b+a

for num in fibo():
    if num>50:
        break

    print(num)


'''
BENEFITS of using GENERATOR over class based ITERATOR:

1. You don't need to define iter() and next() methods
2. You don't need to raise StopIteration exception
'''