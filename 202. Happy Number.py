num=19


def happy_number(num,hsh={}):
    hsh[num] ='true'
    s = sum([int(x)**2 for x in str(num)])
    if s ==1:
        return 'true'
    else:
        if s in hsh:
            return 'false'
        return happy_number(s,hsh)
