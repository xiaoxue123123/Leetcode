grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
]

# 自己写的
# nrow = len(grid)
# ncol = len(grid[0])
#
# visit = [[0]*ncol for i in range(nrow)]
#
# # how to deal with corner case?
# n = 0
# for i in range(nrow):
#     for j in range(ncol):
#         if grid[i][j]=='1' and visit[i][j]==0:
#             print('i',i,'j',j)
#             visit[i][j] = 1
#             if i+1 >= nrow or i-1<0 or j+1 >= ncol or j-1<0:
#                 pass
#             else:
#                 if visit[i+1][j]==0 and visit[i-1][j]==0 and  visit[i][j+1]==0 and  visit[i][j-1]==0:
#                     n+=1
#
#
def is_valid(grid, r, c):
    m, n = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= m or c >= n:
        return False
    return True


import collections
def numIslandsBFS(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                bfs(grid, i, j)
                count += 1
    return count


def bfs(grid, r, c):
    queue = collections.deque()
    queue.append((r, c))
    grid[r][c] = '0'
    while queue:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        r, c = queue.popleft()
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                queue.append((nr, nc))
                grid[nr][nc] = '0'



#
# # 看了网上的DFS，自己写一遍
# def dfs(grid,i,j):
#     if i>=len(grid) or i < 0 or j>=len(grid[0]) or j < 0 or grid[i][j]!='1':
#         return 99
#     grid[i][j]='#'
#     # print(grid)
#     # print('--------')
#     dfs(grid, i+1, j)
#     dfs(grid, i-1, j)
#     dfs(grid, i, j+1)
#     dfs(grid, i, j-1)
#
# res = 0
#
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j]=='1':
#             dfs(grid,i,j)
#             res+=1
#
#





# # 网上的答案:DFS
#
#
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# def dfs(grid, i, j):
#     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
#         return
#     grid[i][j] = '#'
#     dfs(grid, i + 1, j)
#     dfs(grid, i - 1, j)
#     dfs(grid, i, j + 1)
#     dfs(grid, i, j - 1)
#
# if not grid:
#     print(0)
#
# count = 0
# cnt = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         print('--------count',cnt)
#         print('i0,j0',i,j)
#         if grid[i][j] == '1':
#             print('i1,j1',i,j)
#             dfs(grid, i, j)
#             print(grid)
#             print('i,j',i,j)
#             count += 1
#     cnt+=1
# print(count)




