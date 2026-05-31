'''
List comprehension provides a way to transform one list into another
'''

num_list = [1,2,3,4,5,6,7]

'''Using Loop'''
# even = []
# for i in num_list:
#     if i%2 == 0:
#         even.append(i)

print("List Comprehension: ")
print(num_list)

even = [i for i in num_list if i%2 == 0]
print("Even: ",even)

sq_num = [i*i for i in num_list]
print("Square Numbers: ", sq_num, "\n")



print("Set Comprehension: ")
s = set(num_list)
print(s)

'''Set Comprehension'''
even = {i for i in num_list if i%2==0}
print("Even: ",even)

sq_num = {i*i for i in num_list}
print("Square Numbers: ", sq_num, "\n")



print("Dictionary Comprehension: ")
channels = ['Disney XD', 'Nickelodeon', 'CN']
cartoons = ['Kick Buttowski', 'Ninja Hattori', 'Ben 10']

watch = zip(channels, cartoons)
print(watch) #address

for w in watch:
    print(w)

watchAt = {channels:cartoons for channels, cartoons in zip(channels,cartoons)}
print("\n", watchAt)