'''
SET is an unordered collection of unique elements
'''

channels = {'Disney XD', 'Nickelodeon', 'CN', "Nickelodeon"}
print(type(channels))
print(channels, "\n")


#don't initialize the set like this
channels = {} #cuz, this is treated as dictionary
print(type(channels), "\n")


#rather initialize the set like this
a = set()
type(a)
a.add(1)
a.add("hey")
a.add("hey")
print(a, "\n")

num_list = [1,2,2,3,4,5,5,6]
print("List :", num_list)

unique_num = set(num_list)
print("Set: ", unique_num, "\n")

'''Frozen Set: (doesn't allow the changes)'''
fs = frozenset(num_list)
print("Frozen Set: ", fs, "\n")
# fs.add(1) #"NOT ALLOWED"



'''BASIC OPERATIONS'''
print("BASIC SET OPERATIONS: ")
ch1 = {'Disney XD', 'Nickelodeon', 'CN'}
ch2 = {'SuperHungama', 'Disney XD', 'Nick Jr'}

print('CN' in ch1) #True
print('CN' in ch2, "\n") #False

for channel in ch1:
    print(channel)

#UNION (OR Operator)
print("\n","Union: ", ch1|ch2, "\n")

#INTERSECTION (AND Operator)
print("Intersection: ", ch1&ch2, "\n")

#Difference
print("Diiference: ", ch1-ch2, "\n")

#Subset?
print("Ch1 is a Subset of Ch2?: ", ch1<ch2)

ch3 = {'Nick Jr', 'Nickelodeon', 'SuperHungama', 'Disney XD', 'CN'}
print("Ch1 is a Subset of Ch3?: ", ch1<ch3)