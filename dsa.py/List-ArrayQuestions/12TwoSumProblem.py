nums = [5, 9, 1, 2, 4, 15, 6, 3]
n = len(nums)

target = 13


#BRUTE-FORCE APPROACH:
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         if nums[i] + nums[j] == target:
#             print(i, j)

# TC: O( N(N+1)/2 )  ~ O(N)
# SC: O(1)



#OPTIMAL SOLUTION APPROACH:
def twosum(nums):
    hash_map = {}
    for i in range(0, n):
        remaining = target - nums[i]

        if remaining in hash_map:
            return [ hash_map[remaining], i ]
        else:
            hash_map[nums[i]] = i

print(twosum(nums))

# TC: O(N)
# SC: O(N)