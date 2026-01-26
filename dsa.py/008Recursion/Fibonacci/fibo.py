# 0 1 1 2 3 5 8 13

def fibo(n):
    if n==0 or n==1:
        return n

    return fibo(n-1) + fibo(n-2)

ans = fibo(7)
print(ans)

#Time Complexity: O(2^n)
#Space Complexity: O(2^n)