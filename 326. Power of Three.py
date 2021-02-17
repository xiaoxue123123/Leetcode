n = 27

def power_three(n):
    if n == 1:
        print('here1')
        return('true')
    elif n < 3:
        print('here2')
        return 'false'
    else:
        print('here3')
        return power_three(n/3)
