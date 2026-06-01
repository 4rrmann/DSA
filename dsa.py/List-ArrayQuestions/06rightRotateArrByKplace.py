nums = [3, 9, 5, 6, 7, 2]
n = len(nums)

k = 3 #num of rotation
rotations = k%n #writting 'k' but in an Optimized wayy



#BRUTE-FORCE APPROACH:
# for _ in range(rotations):

#     # e = nums.pop()
#     # nums.insert(0, e)


#     temp = nums[n-1]
#     for i in range(n-2, -1,  -1):
#         nums[i+1] = nums[i]

#     nums[0] = temp

# print(nums)

# TC: O(N*r) [r = rotations]
# SC: O(1)



#BETTER SOLUTION APPROACH: (Slicing)
# nums[:] = nums[n-rotations:] + nums[:n-rotations] #TC: O(k) + O(N-k) = O(k +N-k)
# print(nums)

# TC: O(N)
# SC: O(1)



#OPTIMAL APPROACH: (without Slicing)
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left +=1
        right -=1

reverse(nums, n-rotations, n-1)  #Reverse last 'k' elements  [TC: k/2]
reverse(nums, 0, n-rotations -1) #Reverse remaining elements [TC: (N-k)/2]
reverse(nums, 0, n-1)            #Reverse whole array        [TC: N/2]

# TC: k/2 + (N-k)/2 + N/2 =  O(N)
# SC: O(1)

print(nums)
