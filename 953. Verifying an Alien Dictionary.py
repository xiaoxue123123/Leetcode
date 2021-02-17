words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
# create a dictionary for order



# how to know 'app' is shorter than 'apple'? how should i construct the
# for loop

def compare_lex(w1,w2):
    # while len(w1)>0 and len(w2)>0:
    #     l1,w1 = w1[0],w1[1:]
    #     l2,w2 = w2[0],w2[1:]
    #     if dict[l1]>dict[l2]:
    #         return False
    #     elif dict[l1]<dict[l2]:
    #         return True
    #     else:
    #         pass

    for i in range(min(len(w1),len(w2))):
        if dict[w1[i]] > dict[w2[i]]:
            return False
        elif dict[w1[i]] < dict[w2[i]]:
            return True
        else:
            pass

    if len(w1) == 0:
        return True
    if len(w2) == 0:
        return False

def isAlienSorted(words,order):
    dict = {}

    for i, v in enumerate(order):
        dict[v] = i

    for i in range(len(words)):
        for j in range(1,len(words)):
            w1 = words[i]
            w2 = words[j]
            if not compare_lex(w1,w2):
                return False

    return True


print(isAlienSorted(words,order))

# for i in range(len(words)):
#     for j in range(1,len(words)):
#



#
#
# l = 0
# r = len(s)-1
#
# while l<r:
#     if dict[s[l]] < dict[s[r]]:
#         l+=1
#         r-=1
#     else:
#         print('false')
#         break
# print(flag)