nums = [55, 32, -97, 99, 3, 67]
# nums = [-1, -3, -4]

# largest = 0 #doesn't work when all elements are -ve in an array

largest = nums[0]
# largest = float("-inf")

for i in range(0, len(nums)-1):
    # largest = max(largest, nums[i])
    if nums[i] > largest:
        largest = nums[i]

print(largest)

# TC: O(N)
# SC: O(1)