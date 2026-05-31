'''
Generator is a simply way of creating iterator
'''
def next_channel():
    #memory utilization
    yield "Disney XD"
    yield 'Nickelodeon'

itr = next_channel()
print(itr, "\n") #address

print(next(itr))
print(next(itr), "\n")

#through loop also
for channel in next_channel():
    print(channel)

'''
BENEFITS of using GENERATOR over class based ITERATOR:

1. You don't need to define iter() and next() methods
2. You don't need to raise StopIteration exception
'''