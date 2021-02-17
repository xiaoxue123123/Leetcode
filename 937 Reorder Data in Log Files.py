logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

#看了网上答案，自己再写一遍

letters = []
digit = []

for log in logs:
    if log.split(" ")[1].isnumeric():
        digit.append(log)
    else:
        letters.append(log)

letters.sort(key=lambda x: x.split()[0]) # secondary
letters.sort(key=lambda x: x.split()[1:]) # priority
print(letters+digit)







#return value is to be compared, and the value could be a tuple. In such case, it will compare the keywords in the tuple in order. For example, if the 1st element equals, it checks the 2nd element. In this problem, it returns (0, rest, id_) and (1,), and 0 < 1 so that characters are always ahead of digits.
# If they are all characters, the rest will be compared.
# 网上的答案
def f(log):
    id_, rest = log.split(" ", 1) #1的意思说分一个" "
    return (0, rest, id_) if rest[0].isalpha() else (1,)

# letter logs come before number logs
# within letter logs lexicographically.
# digit log in original order

logs = sorted(logs, key = f)