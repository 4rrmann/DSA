nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]

def cons1(nums):
    n = len(nums)
    count = 0
    maxCount = 0

    for i in range(0, n):
        if nums[i] == 1:
            count +=1

        else:
            if count > maxCount:
                maxCount = count
            count = 0

    return max(maxCount, count)

print(cons1(nums))

# TC: O(N)
# SC: O(1)