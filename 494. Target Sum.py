import collections
# def findTargetSumWays(A, S):
#     count = collections.Counter({0: 1})
#     for x in A:
#         step = collections.Counter()
#         for y in count:
#             step[y + x] += count[y]
#             step[y - x] += count[y]
#         count = step
#     return count[S]


A = [1, 1, 1, 1, 1]
S = 3

count = collections.Counter({0: 1})
for x in A:
    step = collections.Counter()
    for y in count:
        print('y',y)
        print('y+x',y+x,'y-x',y-x)
        step[y + x] += count[y]
        step[y - x] += count[y]
        print('step',step)
    count = step



#
# offset = sum(nums)
# dp = [[0 for _ in range(len(nums) + 1)] for _ in range(S + offset + 1)]
#
#
#
# dp[0][offset] = 1
#
# for i in range(1, len(nums)):
#     for j in range(nums[i],2*S+1-nums[i]-1):
#         if dp[i][j]:
#             dp[i - 1][j - nums[i]] += dp[i][j]
#             dp[i - 1][j + nums[i]] += dp[i][j]
#
# print(dp)

# brutal force/DFS 不知道为什么不work
#
# cnt = 0
#
#
# def DFS(prev, i, l, S):
#     global cnt
#     print('prev,l', prev, l)
#     if len(l) - 1 == i:
#         if prev == S:
#             print('here')
#             cnt += 1
#     else:
#         DFS(prev + l[i], i + 1, l, S)
#         DFS(prev - l[i], i + 1, l, S)
#     # return cnt
#
#
# DFS(0, 0, [1, 1], 2)
# print(cnt)