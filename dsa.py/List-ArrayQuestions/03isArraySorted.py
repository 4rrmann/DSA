nums1 = [1, 3, 4, 5, 6, 9]
nums2 = [1, 2, 5, 9, 2, 3]

def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            print("hell naw")
            return
    print("Sorted !")
    return

is_sorted(nums1)
is_sorted(nums2)

#TC: O(N)
#SC: O(1)