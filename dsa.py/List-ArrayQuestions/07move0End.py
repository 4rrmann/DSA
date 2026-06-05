nums = [1, 2, 4, 0, 2, 0, 3, 6, 0, 8]
# nums = [1]
n = len(nums)



#BRUTE-FORCE APPROACH:

# temp = []
# for i in range(0, n):
#     if nums[i] != 0:
#         temp.append(nums[i])

# nz = len(temp)
# for i in range(0, nz):
#     nums[i] = temp[i]

# for i in range(nz, n):
#     nums[i] = 0

# print(nums)



# TC: O(2N) ~ O(N)
# SC: O(N)




#OPTIMAL APPROACH:
def move02end(nums):
    if n==1:
        return

    i=0
    while i<n:
        if nums[i] == 0:
            break
        i+=1

    if i == n:
        return
    

    j=i+1
    while j<n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
        j+=1

move02end(nums)
print(nums)

# TC: O(N)
# SC: O(1)