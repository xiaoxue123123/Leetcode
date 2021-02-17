s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

res = ['' for i in range(len(s))]

for i in s:
    res[indices.pop(0)] = i

print(''.join(res))