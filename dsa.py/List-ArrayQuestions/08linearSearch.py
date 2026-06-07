nums = [1, 3, 4, 5, 2, 6, 9]

def ls(target): 
    n = len(nums)

    for i in range(0, n):
        if nums[i] == target:
            return i
        
    return -1

print(ls(10))

# TC: O(N)
# SC: O(1)