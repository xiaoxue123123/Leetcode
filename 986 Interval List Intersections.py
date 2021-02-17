A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

# 自己的答案，很慢，过了
def join_two_pair(a,b):
    if b[0]<a[1] and b[1]>a[0]:
        return [max(a[0],b[0]),min(a[1],b[1])]
    if b[1] == a[0]:
        return [b[1],b[1]]
    if a[1]==b[0]:
        return [b[0],b[0]]

res = []
for i in range(len(A)):
    for j in range(len(B)):
        union = join_two_pair(A[i], B[j])
        if union:
            res.append(union)


# 网上的答案

ans = []
i = j = 0

while i < len(A) and j < len(B):
    # Let's check if A[i] intersects B[j].
    # lo - the startpoint of the intersection
    # hi - the endpoint of the intersection
    lo = max(A[i][0], B[j][0])
    hi = min(A[i][1], B[j][1])
    if lo <= hi:
        ans.append([lo, hi])

    # Remove the interval with the smallest endpoint
    if A[i][1] < B[j][1]:
        i += 1
    else:
        j += 1


# 网上的答案自己再写一遍,还是没能写出来
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
i = 0
j = 0
res = []
# for _ in range(6):
#     print('round',_)
while i <len(A) and j<len(B):
    if A[i][1]>=B[j][0] and A[i][0]<=B[j][1]:
        res.append([max(A[i][0],B[j][0]),min(A[i][1],B[j][1])])
        if i <len(A)-1:
            i+=1
    print('i',i)
    if i == len(A)-1 or B[j][1]<A[i][0] :
        j+=1
    print('j',j)
    print('i2',i)


