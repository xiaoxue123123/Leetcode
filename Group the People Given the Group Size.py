s = [3,3,3,3,3,1,3]
d = {}
res = []
for i in range(len(s)):
    e = s[i]
    if e not in d.keys():
        d[e] = [i]
    else:
        if e > len(d[e]):
            d[e].append(i)
    if e==len(d[e]):
        res.append(d[e])
        d[e] = []