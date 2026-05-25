nums = [3, 5, 6, 4, 0, 8, 9, 10, 7, 1]

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:     #aescending
        # while j>=0 and nums[j]<key:   #descending
            nums[j+1], nums[j] = nums[j], nums[j+1]
            j -=1
        nums[j+1] = key
    print(nums) 

insertion_sort(nums)

#TC: O(N(N+1)/2) ~ O(N*N)
#SC: O(1)