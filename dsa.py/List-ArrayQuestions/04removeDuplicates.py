#Given: Sorted Array
nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# nums = [3]
n = len(nums)

#BRUTE-FORCE APPROACH:

# freq_map = {}
# for i in range(0, n):
#     freq_map[nums[i]] = 0 #{1: 0, 2: 0, 3: 0, 4: 0, 7: 0, 9: 0, 10: 0}

# j = 0
# for k in freq_map:
#     nums[j] = k
#     j+=1

# print(nums)
# print(j)

#TC: O(N+N) ~ O(N)
#SC: O(N)



#OPTIMAL APPROACH: (two-pointers)

#edge case
if n == 1:
    print(1)

i = 0
j = i+1

while j<n:
    if nums[i] != nums[j]:
        i+=1
        nums[i], nums[j] = nums[j], nums[i]
    
    j+=1

print(nums)
print(f"Unique Elements: {i+1}")