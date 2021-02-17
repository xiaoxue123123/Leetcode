#s = "A man, a plan, a canal: Panama"
s = "  "
# solution 1:
# import re
# s = re.sub(r'[\W_]+', ' ', s)
# s = s.lower()
# s = s.replace(' ','')
# print(s==s[::-1])

# solution 2: use two pointers

p0 = 0
pn = len(s)-1
flag = True

while p0<pn:
    while p0<pn and not s[p0].isalnum():
        print('s[p0]',s[p0])
        p0 += 1
    while p0<pn and not s[pn].isalnum():
        print('s[pn]',s[pn])
        pn -= 1
    if s[p0].lower() != s[pn].lower():
        print('s[p0]',s[p0])
        print('s[pn]',s[pn])
        flag = False
        break
    else:
        p0 += 1
        pn -= 1
print(flag)