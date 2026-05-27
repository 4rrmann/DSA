nums = [55, 32, -97, 99, 3, 67]

#BRUTE-FORCE APPROACH:

# nums.sort()
# print(nums)
# print(nums[-2])

#TC: O(N*logN)
#SC: O(1)



#BETTER APPROACH:

# largest = float("-inf")
# second_largest = float("-inf")

# for i in range(0, len(nums)):
#     largest = max(largest, nums[i])

# for i in range(0, len(nums)):
#     if nums[i] > second_largest and nums[i] != largest:
#         second_largest = nums[i]

# print(largest)
# print(second_largest)

#TC: O(N+N) = O(2N)  ~ O(N)
#SC: O(1)



#OPTIMAL APPROACH:
largest = float("-inf")
second_largest = float("-inf")

for i in range(0, len(nums)):

    # largest = max(largest, nums[i])
    # if nums[i] > second_largest and nums[i] != largest:
    #     second_largest = nums[i]

    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]


print(f"l: {largest}")
print(f"sl: {second_largest}")

#TC: O(N)
#SC: O(1)