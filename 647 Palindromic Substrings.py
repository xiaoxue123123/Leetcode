

# 我自己的solution, time out 了
# total = len(s)
#
#
# def is_palindrom(s):
#     i = 0
#     j = len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
#
#
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if is_palindrom(s[i:j + 1]):
#             total += 1
# return total

# 网上的solution 1：
s =  "abc"

cnt = 0
def is_palindrom(s,i,j,cnt):
    while i >=0 and j <len(s) and s[i] == s[j]:
        cnt +=1
        i-=1
        j+=1
    return cnt

for i in range(len(s)):
    cnt = is_palindrom(s, i, i, cnt) # odd number
    cnt = is_palindrom(s, i, i+1, cnt) # even number


# 网上的solution 2: DP
def countSubstrings(s) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    res = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            dp[i][j] = s[i] == s[j] and ((j - i + 1) < 3 or dp[i + 1][j - 1])
            # dp[i + 1][j - 1] is referred to the string in between dp[i][j],
            # which is the last status before expanding to dp[i][j], that's why we are using dp.
            # you should explain why you use dp[i+1][j-1] to calculate dp[i][j].
            # The reason is that i is in descending order and j is in ascending order
            res += dp[i][j]
    return res
