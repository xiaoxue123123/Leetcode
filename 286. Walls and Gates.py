rooms = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]


def wallsAndGates(rooms):
    # find index of doors (if not r tells doors)
    q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
    for i, j in q:
        for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                print(rooms[i][j])
                rooms[I][J] = rooms[i][j] + 1
                q += (I, J),
    return rooms




for i, row in enumerate(rooms):
    for j, r in enumerate(row):
        if not r:
            print(r)
            print(i,j)

for i, row in enumerate(rooms):
    print(i,row)