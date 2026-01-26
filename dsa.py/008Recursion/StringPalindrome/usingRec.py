s = "NITIN"

# left = 0
# right = len(s) -1

def palindrome(s, left, right):
    if left >=right:
        return True

    if s[left] != s[right]:
        return False
    
    return palindrome(s, left+1, right-1)

x = palindrome(s, 0,len(s)-1)
print(x)

#The function compares characters recursively from both ends and returns False on mismatch, otherwise continues until the base condition is reached.

#Time Complexity: O(N/2) ~ O(N)
#Space Complexity: O(N/2) ~ O(N) --> Stack space