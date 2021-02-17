s = "lee(t(c)o)de)"

# my own solution 1: 和答案里面的Approach 2: Two Parse String Builder一样
# def remove(s,reverse):
#     left = 0
#     right = 0
#
#
#     s = list(s)
#
#     for i in range(len(s)):
#         if s[i] == '(':
#             left += 1
#         if s[i] == ')':
#             right += 1
#         if left < right and not reverse:
#             # constraint: has to be left >= right
#             s[i] = ''
#             right -= 1
#         if left > right and reverse:
#             # need to reverse string
#             # constraint: has to be right >= left
#             s[i] = ''
#             left -= 1
#     return(''.join(s))
#
#
# s = remove(s,False)
# s = remove(s[::-1],True)

# my own solution 2
# use two pointer
s = "))(("
s = list(s)
stk = []
for i in range(len(s)):
    if s[i] == '(':
        stk.append(i)
    if s[i] == ')':
        if stk:
            s[i] = ''
        else:
            stk.pop()

if len(stk)>0:
    for i in stk:
        s[i] = ''


# 网上的答案
s = "))(("
s = "lee(t(c)o)de)"
#到有了配对的再放进去
stack, ret = [], ['']*len(s)
for i,c in enumerate(s):
    print('i',i,'c',c)
    if c=='(':
        stack.append(i)
    elif c==')':
        if stack:
            left=stack.pop()
            ret[left] = s[left]
            ret[i] = c
    else:
        ret[i] = c
    print('ret',ret)