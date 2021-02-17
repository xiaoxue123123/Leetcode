numRows = 5

# solution 3 is faster than solution 1: maybe directly modifying element
# is faster than append? 

# dynamic programming
# solution 1: passed. But time complexity and space complexity bad.
res = []

def next_pascal(l):
    mid = []
    for i in range(1,len(l)):
        mid.append(l[i-1]+l[i])
    return([1]+mid+[1])

for i in range(1,numRows+1):
    if i==1:
        res.append([1])
    elif i ==2:
        res.append([1,1])
    else:
        res.append(next_pascal(res[-1]))


# solution 2: 网上的答案
res = [[1]]
for i in range(1, numRows):
    res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
res[:numRows]

# explanation: Any row can be constructed using the offset sum of the previous row. Example:
#
#     1 3 3 1 0
#  +  0 1 3 3 1
#  =  1 4 6 4 1

# solution 3: 网上的答案

res = [[1] * (i + 1) for i in range(numRows)]
for i in range(2, numRows):
    for j in range(1, i):
        res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
