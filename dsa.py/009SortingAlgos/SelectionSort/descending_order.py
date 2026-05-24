nums = [5, 7, 3, 8, 4, 1, 6, 9, 2]

def selection_sort_dec(nums):
    for i in range(0, len(nums)-1):
        high_idx = i
        for j in range(i+1, len(nums)):
            if nums[high_idx] < nums[j]:
                high_idx = j
        nums[i], nums[high_idx] = nums[high_idx], nums[i]
    print(nums)

selection_sort_dec(nums)

#TC: O(N*N)
#SC: O(1)