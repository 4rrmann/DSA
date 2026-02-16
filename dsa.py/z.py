s = "ARMANNAMRA"

def palindrome(s, l,r):
    if l>=r:
        return True

    if s[l] != s[r]:
        return False

    return palindrome(s, l+1,r-1)

print("is this a Palindrome?")
print(palindrome(s, 0,len(s)-1))

