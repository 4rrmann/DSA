nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)

submax = float("-inf")

#BRUTE-FORCE APPROACH:
# for i in range(0, n):
#     total = 0
#     for j in range(i, n):
#         total += nums[j]
#         submax = max(submax, total)

# print(submax)

# TC: O( N(N+1)/2 )  ~ O(N)
# SC: O(1)



#OPTIMAL SOLUTION APPROACH: (Kadane's algorithm)
total = 0
for i in range(0, n):
    total+= nums[i]

    if total>=0:
        submax = max(total, submax)

    else:
        total = 0

print(submax)

# TC: O(N)
# SC: O(1)