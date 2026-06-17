prices = [7, 2, 1, 5, 6, 4, 8]
n = len(prices)


#BRUTE-FORCE APPROACH:
# max_profit = 0
# for i in range(0, n):
#     for j in range(i+1, n):
#         if prices[j] > prices[i]:
#             p = prices[j] - prices[i]
            
#             if p>max_profit:
#                 max_profit = p

# print(max_profit)

# TC: O( N(N+1)/2 )  ~ O(N)
# SC: O(1)



#OPTIMAL SOLUTION APPROACH:
min_price = float("inf")
max_profit = 0

for i in range(0, n):

    if prices[i]<min_price:
        min_price = prices[i]

    profit = prices[i] - min_price

    if profit>max_profit:
        max_profit = profit

print(max_profit)

# TC: O(N)
# SC: O(1)
