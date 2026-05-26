nums = [4, 1, 7, 6, 3, 2, 8]
#       0  1  2  3  4  5  6


def partition(nums, low,high):
    pivot = nums[low]
    i,j = low,high
    while i<j:
        while nums[i] <= pivot and i<=high-1: #if not then 'i' set
            i+=1
        while nums[j] >= pivot and j>=low+1: #if not then 'j' set
            j-=1

        #now, we have to swap i <-> j based on the setted ones above!
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    #i>j
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quickS(nums, low,high):
    if low<high:
        p_idx = partition(nums, low,high)
        quickS(nums, low,p_idx-1)
        quickS(nums, p_idx+1,high)
    return


quickS(nums, 0,len(nums)-1)
print(nums)

#TC: O(N*logN) {best/avg case}
#TC: O(N*N) {worst case: [x, x, x, x, x, .., x]}
#SC: O(1) (no extra space used, changes occured inside the array)