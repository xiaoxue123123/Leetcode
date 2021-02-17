A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

#### solution1
# 网上看的别人的solution
import collections
# 先用counter找出每种a+b value的值和freq
AB = collections.Counter(a + b for a in A for b in B)
# 再去找在c+d有多少和是AB里面值的负数，然后把freq 加起来
# AB[-c - d] 找的是AB里面的freq, 整个list里面是每个-c-d的value对应的
# AB的freq.
print(sum(AB[-c - d] for c in C for d in D))
# 核心是：1. 用collections.Counter算freq
# 2. 用 -c-d去AB里面找
# 3. A,B,C,D combination = AB的combination freq + 每个CD

#### solution2

res, d = 0, {}

#手动实现collections.Counter
for n1 in A:
    for n2 in B:
        tmp = n1 + n2
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1

#手动实现把AB里面的freq加起来
for n1 in C:
    for n2 in D:
        tmp = 0 - (n1 + n2)
        if tmp in d:
            res += d[tmp]