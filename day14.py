import day10

DATA = "stpzcrnm"
TDATA = "flqrgnkx"

def get_rowstr(d, i):
    s = d + "-" + str(i)
    h = day10.fullHash(s, list(range(256)))
    #print(h)
    rowstr = ""
    for char in h:
        rowstr += '{:0>4}'.format(bin(int(char, 16))[2:])
    return rowstr

def count_total_used(d):
    used = 0
    for i in range(128):
        s = get_rowstr(d, i)
        used += s.count('1')
    return used

def get_grid(d):
    grid = []
    for i in range(128):
        grid.append(list(get_rowstr(d, i)))
    return grid

def get_neighbors(i, j):
    neighbors = []
    if i-1 >= 0:
        neighbors.append((i-1, j))
    if i+1 < 128:
        neighbors.append((i+1, j))
    if j-1 >= 0:
        neighbors.append((i, j-1))
    if j+1 < 128:
        neighbors.append((i, j+1))
    return neighbors

def find_region(grid, i, j, r):
    to_check = get_neighbors(i, j)
    while len(to_check) > 0:
        node = to_check.pop()
        if grid[node[0]][node[1]] == "1":
            grid[node[0]][node[1]] = r
            to_check += get_neighbors(node[0], node[1])
    return grid

def get_regions(d):
    regions = 2
    grid = get_grid(d)
    for i in range(128):
        for j in range(128):
            if grid[i][j] == "1":
                grid[i][j] = str(regions)
                grid = find_region(grid, i, j, str(regions))
                regions += 1
    print(str(regions-2))
    #return regions
    return grid
