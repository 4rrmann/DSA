nums = [1, 0, 3, 4]



#BRUTE-FORCE APPROACH:
# for i in range(0, len(nums)+1):
#     if i not in nums:
#         print(i)

# TC: O(N*N)
# SC: O(1)



#BETTER SOLUTION APPROACH: (using Dict)
# freq = {}

#  #O(N)
# for i in range(0, len(nums)+1):
#     freq[i] = 0 #initialize (nums:0)

#  #O(N)
# for num in nums:
#     if num in freq:
#         freq[num] +=1

#  #O(N)
# for k,v in freq.items():
#     if v == 0:
#         print(k)

# TC: O(3N) ~ O(N)
# SC: O(1)



#OPTIMAL SOLUTION APPROACH: (sum)
n = len(nums)
#sum of first "n" natural numbers
tsum = (n * (n+1)) / 2

nsum = 0
for i in range(0, len(nums)):
    nsum += nums[i]

mis = tsum - nsum
print(int(mis))

# TC: O(N)
# SC: O(1)