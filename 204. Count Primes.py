n = 10



# 自己写的
l = [1]*n
l[0] = l[1] = 0

for i in range(2,n):
    if l[i] == 1:
        print('n//i',n//i)
        for j in range(2,n//i): # 找到小于n，所有i的倍数。
            # 如果用n//i，i=3,j<3,j只能取到2
            # 如果用n//i+1, i=2,j<6,j会取到5
            # 所以只能用(n-1)//i+1，取到的j不会超过10。(n-1)//i不会超过10，+1确保不会有剩余。
            print('i',i,'j',j)
            l[i*j] = 0
print(sum(l))

















# 网上的答案

# Sieve of Eratosthenes


# if n < 2:
#     print(0)
#
# strikes = [1] * n
#
# strikes[0] = 0
# strikes[1] = 0
#
# for i in range(2, int(n ** 0.5) + 1):
#     if strikes[i] != 0:
#         strikes[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
# print(sum(strikes))