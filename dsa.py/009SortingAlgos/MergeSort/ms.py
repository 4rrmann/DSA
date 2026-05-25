arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]


def m2sa(left, right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        
        else:
            # left[i] > right[j]
            result.append(right[j])
            j+=1

    if i<n:
        while i<n:
            result.append(left[i])
            i+=1

    if j<m:
        while j<m:
            result.append(right[j])
            j+=1

    return result


# mid = len(arr)//2

# left_arr = arr[:mid]
# print(left_arr)

# right_arr = arr[mid:]
# print(right_arr)

 
def merge_sort(arr):
    #base-case
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return m2sa(left, right)

x = merge_sort(arr)
print(x)