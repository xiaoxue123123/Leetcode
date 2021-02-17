num1 = '1'
num2 = '9'

res = []
carry = 0
i1 = len(num1) - 1
i2 = len(num2) - 1

while i1 >= 0 or i2 >= 0:
    if i1 >= 0:
        x1 = ord(num1[i1]) - ord('0')
    else:
        x1 = 0
    if i2 >= 0:
        x2 = ord(num2[i2]) - ord('0')
    else:
        x2 = 0
    value = (x1 + x2 + carry) % 10
    carry = (x1 + x2 + carry) // 10
    res.append(value)
    i1 -= 1
    i2 -= 1

if carry>0:
    res.append(carry)

print (''.join([str(i) for i in res[::-1]]))