
# 网上的答案，自己写一遍，sliding window,
# 一步步slide，移出slide出来的element

s = "cbaebabacd"
p = "abc"
import collections

hp = collections.Counter(list(p))
hs = collections.Counter()
np = len(p)
i=0
res = []

for i in range(len(s)):
    # if collections.Counter(list(s[i:i+len(p)])) == hp:
    #     res.append(i)
    hs[s[i]] += 1
    if i>=np: ## use i>=np 因为要slide出来了再清理,i是index，所以当i==np时
        # 其实已经比np长了
        if hs[s[i-np]]==1:
            del hs[s[i-np]]
        else:
            hs[s[i-np]]-=1
    if hs==hp:
        res.append(i-np+1)
















# while i < len(s):
#     if s[i] in h and h[s[i]]>0:
#         h[s[i]] -=1
#     if s[i] not in h:
#         h = collections.Counter(list(p))
#     if s[i] in h and h[s[i]]==0 and sum(h.values())>0:
#
#     if sum(h.values())==0:
#         res.append(i-len(p)+1)
#         h[s[i-len(p)+1]] = 1
#     i += 1
#print(res)



