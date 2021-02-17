nums = [1,2,3]

# 通过我学习DFS之后写出的
# recursion: 递归
def permute(nums):

    res = []
    def DFS(nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            DFS(nums[:i]+nums[i+1:],path+[nums[i]],res)
            # 核心是不断把nums里面的num移到path里面，
            # 当nums里面没有num剩下了（或者len(path)==3,nums最开始的长度），就把path加到res里

    DFS(nums,[],res)
    return res

print(permute(nums))
# backtracking: 回溯法
def permute(nums):
    res=[]
    visited = [0] * len(nums)
    def DFS(path):
        if len(path)==len(nums):
            res.append(path)
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = 1
                DFS(path+[nums[i]]) # 不断在path里面加element，如果visited过了，就不加
                # 如果没有visited,就加。
                # 如果在这一个path里面，visited过了，就等于1。跳出这个path，再把visited变回0。
                visited[i] = 0
    DFS([])

    return res
print(permute(nums))





















# # # 网上的答案
# # # DFS
# def permute(nums):
#     res = []
#     dfs(nums, [], res)
#     return res
#
#
# def dfs(nums, path, res):
#     if not nums: # 当不剩nums的时候，append path.
#         res.append(path)
#         # return # backtracking
#     for i in range(len(nums)):
#         print('i',i)
#         print('nums[:i] + nums[i + 1:]',nums[:i] + nums[i + 1:])
#         print('path + [nums[i]]',path + [nums[i]])
#         print('res',res)
#         dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# 网上的solution 2

# def permute(nums):
#     perms = [[]]
#     for n in nums:
#         new_perms = []
#         for perm in perms:
#             print('perm',perm)
#             for i in range(len(perm)+1):
#                 print('i',i)
#                 new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
#                 print('new_perms',new_perms)
#         perms = new_perms
#     return perms

