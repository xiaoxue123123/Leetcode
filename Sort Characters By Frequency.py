### 没做完 因为还没学过hash map 
s = "tree"
freq = {}
res = []
l = 't'

def compare(res,l,freq,pos):
    if l not in freq.keys():
        freq[l] = 1
        res.append(l)
    else:
        freq[l] += 1
        if freq[l] <= freq[res[pos]]:
            res.append(l)
        else:
            last = res[pos]
            res = res[:pos]
            res.append(l)
            res.append(last)
    compare(res, l, freq,pos)