s = "3[a10[c]]"

# 看过答案之后自己写一遍

stack = []
curnum = 0
curstring = ''
num = 0
prestring = ''
for c in s:
    if c.isdigit():
        curnum = curnum*10+int(c)
    elif c == '[':
        stack.append(curstring)
        stack.append(curnum)
        curnum = 0
        curstring = ''
    elif c.isalpha():
        curstring = curstring + c
    else:
        num = stack.pop()
        prestring = stack.pop() #what if num is more than 1 digit
        curstring = prestring + num*curstring











#
#
#
# # 网上的答案
# stack = [] #use a stack to save previous parsed letter
# curNum = 0
# curString = ''
# for c in s:
#     if c == '[':#每次遇到[就把原来的num和string 加进去stack里面
#         stack.append(curString)
#         stack.append(curNum)
#         curString = ''
#         curNum = 0
#     elif c == ']': #每次遇到]就把stack里面的[之前的num和previous string加到curstring里
#         # curstring进行迭代更新
#         num = stack.pop()
#         prevString = stack.pop()
#         curString = prevString + num * curString
#     elif c.isdigit():
#         curNum = curNum * 10 + int(c)
#     else:
#         curString += c
# print(curString)