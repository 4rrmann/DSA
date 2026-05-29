nums = [5, -2, 3, 4, 6, 7, 10]
n = len(nums)

#SLICING:
# nums[:] = [nums[n-1]] + nums[0:n-1] #in-place change in a same address variable

#LOOP:
temp = nums[n-1]

for i in range(n-2, -1,  -1):
    nums[i+1] = nums[i]

nums[0] = temp

print(nums)

#TC: O(N)
#SC: O(1)