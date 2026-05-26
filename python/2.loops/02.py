# numbers = [1,2,3,4,5,6,7,8,9]

# sum = 0
# for i in numbers:
#     if i%2 == 0:
#         sum += i

# print(f"sum of even numbers: {sum}")

n = 10

sum = 0
for i in range(1, n+1):
    if i%2 == 0:
        sum +=i

print(f"Sum of even numbers: {sum}")