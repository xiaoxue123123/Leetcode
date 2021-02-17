import collections

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

deadends = set(deadends)


def neighbor(node):
    res = []
    for i in range(4):

        print('n pre change',n)
        for direction in [1, -1]:
            n = int(node[i])
            print(direction)
            n = (n + direction) % 10
            print('n',n)
            res.append(node[:i] + str(n) + node[i + 1:])
    return res


seen = ['0000']
q = [('0000', 0)]
while q:
    node, d = q.pop(0)
    if node == target: print(d)
    if node in deadends:
        continue
    neis = neighbor(node)
    for nei in neis:
        if nei not in seen:
            seen.append(nei)
            q.append((nei, d + 1))

#
# def openLock(deadends, target):
#     def neighbors(node):
#         for i in range(4):
#             x = int(node[i])
#             for d in (-1, 1):
#                 y = (x + d) % 10
#                 yield node[:i] + str(y) + node[i + 1:]
#
#     dead = set(deadends)
#     queue = collections.deque([('0000', 0)])
#     seen = {'0000'}
#     while queue:
#         node, depth = queue.popleft()
#         if node == target: return depth
#         if node in dead: continue #go to next element in loop
#         for nei in neighbors(node):
#             if nei not in seen:
#                 seen.add(nei)
#                 queue.append((nei, depth+1))
#     return -1
#


