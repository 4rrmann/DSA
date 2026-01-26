s = "NITIN"

left = 0
right = len(s) -1

is_palindrome = True

while left<right:

    if s[left] != s[right]:
       is_palindrome = False
       break

    left +=1
    right -=1

print(is_palindrome)

# Time Complexity: O(n/2) ~ O(n)
# Space: O(1)