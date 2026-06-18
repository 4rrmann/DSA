nums = [5, 10, -3, -1, -10, 6]
n = len(nums)

#BRUTE-FORCE APPROACH:
# result = []
# pos = []
# neg = []

# for i in range(0, n):
#     if nums[i]>0:
#         pos.append(nums[i])
#     elif nums[i] < 0:
#         neg.append(nums[i])

# print(f"Positive List: {pos}")
# print(f"Negative List: {neg}")

# for i in range(0, len(pos)):
#     nums[2*i] = pos[i]
#     nums[2*i +1] = neg[i]

# print(f"\nRearrange Array Elements by Sign:\n{nums}")

# TC: O( N + N/2 )  ~ O(N)
# SC: O(N/2 + N/2)  ~ O(N)

       

#OPTIMAL SOLUTION APPROACH:
result = [0] * n
posIdx, negIdx = 0, 1

for i in range(0, n):
    if nums[i] >=0:
        result[posIdx] = nums[i]
        posIdx +=2
    else:
        result[negIdx] = nums[i]
        negIdx +=2

print(f"\nRearrange Array Elements by Sign:\n{result}")

# TC: O(N)
# SC: O(1)[I've to return that 'result'] / O(N)