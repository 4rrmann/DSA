nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
n = len(nums)



#BRUTE-FORCE APPROACH:
# maxCount = 0

# for i in range(0, n):
#     num = nums[i]
#     count = 1
#     while num +1 in nums:
#         count +=1
#         num = num +1

#     if maxCount<count:
#         maxCount = count


# print(maxCount)

# TC: O(N*N)
# SC: O(1)



#BETTER SOLUTION APPROACH:
# nums.sort()     #[1, 1, 1, 2, 3, 5, 98, 99, 100, 101]

# count = 0
# last_smaller = float("-inf")
# maxCount = 0

# for i in range(0, n):
#     num = nums[i]
#     if num -1 == last_smaller:
#         count +=1
#         last_smaller = num

#     elif num-1 != last_smaller:
#         count =1
#         last_smaller = num

#     maxCount = max(maxCount, count)


# print(maxCount)

# TC: O(NlogN + N)
# SC: O(1)



#OPTIMAL SOLUTION APPROACH:
my_set = set()

for i in range(0, n):
    my_set.add(nums[i]) #O(N)

maxCount = 0

for num in my_set: #O(N)
    if num-1 not in my_set:
        x = num
        count = 1
        while x+1 in my_set: #O(N)
            count +=1
            x +=1

# The while loop did NOT run 'N' times for each number, it ran only once for the entire sequence.

        maxCount = max(maxCount, count)

print(maxCount)

# TC: O(N + N + N) ~ O(N)
# SC: O(N)