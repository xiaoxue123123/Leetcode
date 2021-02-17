n=3

res = [0]*(n+1)

if n>=0:
    res[0] = 0
if n>=1:
    res[1] = 1
if n>=2:
    res[2] = 1
if n>=3:
    for i in range(2,n):
        res[i+1]=res[i-1]+res[i]
print(res[n])

