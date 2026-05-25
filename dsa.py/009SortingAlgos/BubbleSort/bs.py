nums = [5, 7, 3, 8, 4, 1, 6, 9, 2]
# nums = [1,2,3,4,5]

def bubble_sort(nums):
    n = len(nums)

    for i in range(n-2,-1, -1):
        is_swap = False

        for j in range(0, i+1):

            if nums[j] > nums[j+1]:     #aescending
            # if nums[j] < nums[j+1]:   #descending
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True

        # No swaps happened
        if is_swap == False:

            # if first pass itself had no swap
            if i == 0:
                print("Array became sorted early")

            else:
                print("Already in Best Case")

            print(nums)
            return

    print(nums)

bubble_sort(nums)

'''Avg/worst Case'''
#TC: O(N*N)
#SC: O(1)

'''Best Case'''
#TC: O(N)
#SC: O(1)