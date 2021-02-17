# 121

prices = [7,1,5,3,6,4]

max_profit = 0
min = 10000000000
l = len(prices)

for p in prices:
    if p < min:
        min = p
    # if smaller, update min
    # if bigger, check with max_profit and see if update
    else:
        diff = p - min
        if diff > max_profit:
            max_profit = diff
print(max_profit)







# for i in range(l):
#     for j in range(i+1,l):
#         diff = prices[j] - prices[i]
#         if i<j and diff > max:
#             max = diff

# max_pro = 0
# cur_pro = 0
# for i in range(1, len(prices)):
#     cur_pro = prices[i] - (prices[i - 1] - cur_pro)
#     if cur_pro < 0:
#         cur_pro = 0
#     max_pro = max(cur_pro, max_pro)


