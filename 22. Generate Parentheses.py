
n = 3
# constrait l_n <= r_n
res = []
# use backtracking
def dfs(n,path,res,l_n,r_n):
    if len(path) == 2*n:
        res.append(path)
    if l_n>r_n: # 如果open比close的多，加close
        new_path = path+')'
        dfs(n, new_path, res,l_n,r_n+1)
    if l_n<n: #如果open还没有到max(n)，加open
        new_path = path +'('
        dfs(n, new_path, res,l_n+1,r_n)


dfs(3,'',res,0,0)


#
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         dp = [[] for i in range(n + 1)]
#         dp[0].append('')
#         for i in range(n + 1):
#             print('i',i)
#             for j in range(i):
#                 print('j',j)
#                 #dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
#                 for x in dp[j]:
#                     print('x',x)
#                     for y in dp[i-j-1]:
#                         print('y',y)
#                         dp[i] += '(' + x + ')' + y
#                         print('dp[i]',dp[i])
#                     print('dp after y loop',dp)
#                 print('dp after x loop',dp)
#         return dp[n]
#
# a = Solution()
# a.generateParenthesis(3)