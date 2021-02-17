    # freq = []
    # is_unique = []
    # letter_map = {}
    # unique_order = {} # map po in freq list
    # unique_cnt = 0 # curr po in freq list
    # for i in range(len(s)):
    #     l = s[i] # initiate letter
    #     if l not in unique_order.keys():
    #         unique_order[l] = unique_cnt
    #         unique_cnt += 1
    #         freq.append(1)
    #         is_unique.append(True)
    #     else:
    #         freq_po = unique_order[l]
    #         freq[freq_po] += 1
    #         is_unique[freq_po] = False
    #     if freq[first_unique_po] > 1:
    #         first_unique_po += 1
    # if freq[first_unique_po]
s = 'loveleetcode'
unique = []
m = {}
order = 0
for i in range(len(s)):
    l = s[i]
    print(l)
    if l not in m.keys():
        unique.append(l)
        m[l] = order
    else:
        if l in unique:
            unique.remove(l)
    order += 1
    print('m', m)
    print('unique', unique)
if len(unique) > 0:
    print(m[unique[0]])
else:
    print(-1)