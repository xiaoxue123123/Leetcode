s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

# wordDict = {v:0 for v in wordDict}



# 看了答案 DP
dp = [0 for _ in range(len(s)+1)]
dp[0] = 1
j=0
for i in range(len(s)+1):
    print('i,j',i,j)
    for j in range(0,i):
        print('s[j:i]', s[j:i])
        if (dp[j] and s[j:i] in wordDict):
            print('here')
            dp[i] = 1

print(dp[len(s)])


#
# match = []
# j=0
# for i in range(len(s)+1):
#     if s[j:] in wordDict:
#         print(True)
#         break
#     if s[j:i] in wordDict:
#         print('s[j:i]', s[j:i])
#         match += s[j:i]
#         j=i
# print(''.join(match) == s)
