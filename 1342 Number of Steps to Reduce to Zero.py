num = 8
cnt = 0
if num == 0:
    cnt = 0



while num != 0:
    if num % 2 == 0:
        num = num/2
        cnt += 1
    else:
        num = num -1
        cnt +=1
print(cnt)
