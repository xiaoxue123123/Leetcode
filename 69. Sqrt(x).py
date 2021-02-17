x = 10

l,r = 0,x

res = 0
while res == 0:
    mid = l + (r-l)//2
    res = 0
    if x >= mid**2 and x < (mid+1)**2:
        res = mid
    elif x < mid**2:
        r = mid
    else:
        l = mid + 1