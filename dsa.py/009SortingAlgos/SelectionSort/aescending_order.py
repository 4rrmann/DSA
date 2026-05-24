nums = [5, 7, 3, 8, 4, 1, 6, 9, 2]

def selection_sort_aes(nums):
    for i in range(0, len(nums)-1):
        mini_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[mini_idx]:
                mini_idx = j
        nums[i], nums[mini_idx] = nums[mini_idx], nums[i]
    print(nums)

selection_sort_aes(nums)

#TC: O(N*N)
#SC: O(1)