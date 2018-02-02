import math

def is_down(k):
    n = 0
    while ((2*n + 1)**2 - n) < k:
        n += 1
    if (2*n + 1)**2 - n == k:
        return n
    return False

def is_right(k):
    n = 0
    while ((2*n - 1)**2 + n) < k:
        n += 1
    if (2*n - 1)**2 + n == k:
        return n
    return False

def is_left(k):
    n = 0
    while ((2*n)**2 + (n+1)) < k:
        n += 1
    if (2*n)**2 + (n+1) == k:
        return n
    return False

def is_up(k):
    n = 0
    while (2*n)**2 - (n-1) < k:
        n += 1
    if (2*n)**2 - (n-1) == k:
        return n
    return False

def is_plus(k):
    '''
    #down
    r = (math.sqrt((16*k)-7) - 3)
    if r/8 == int(r/8):
        return int(r/8)
    #left
    #right
    #up
    '''
    if is_up(k):
        return is_up(k)
    if is_down(k):
        return is_down(k)
    if is_left(k):
        return is_left(k)
    if is_right(k):
        return is_right(k)
    return False

def is_up_left(k):
    n = 0
    while (2*n)**2 + 1 < k:
        n += 1
    if (2*n)**2 + 1 == k:
        return 2*n
    return False

def is_low_left(k):
    n = 0
    while (2*n)**2 + 1 + (2*n) < k:
        n += 1
    if (2*n)**2 + 1 + (2*n) == k:
        return 2*n
    return False

def is_low_right(k):
    n = 0
    while (2*n + 1)**2 < k:
        n += 1
    if (2*n + 1)**2 == k:
        return 2*n
    return False

def is_up_right(k):
    n = 0
    while (2*n)**2 + 1 + (4*n) < k:
        n += 1
    if (2*n)**2 + 1 + (4*n) == k:
        return 2*n
    return False

def is_diag(k):
    if is_up_left(k):
        return is_up_left(k)
    if is_low_left(k):
        return is_low_left(k)
    if is_low_right(k):
        return is_low_right(k)
    if is_up_right(k):
        return is_up_right(k)
    return False

def get_side(k):
    v = math.sqrt(k)
    if math.floor(v) % 2 == 1:
        lower_square = math.floor(v)
        upper_square = math.floor(v)+2
    else:
        lower_square = math.floor(v)-1
        upper_square = math.floor(v)+1
    n = (lower_square + 1) // 2
    top_left = 4*(n**2) + 1
    bot_left = 4*(n**2) + (2*n)
    bot_right = 4*(n**2) + 1 + (4*n)
    top_right = 4*(n**2) + 1 - (2*n)
    if top_right < k < top_left:
        return "top"
    elif top_left < k < bot_left:
        return "left"
    elif bot_left < k < bot_right:
        return "bottom"
    else:
        return "right"

def take_step(k, side):
    v = math.sqrt(k)
    if math.floor(v) % 2 == 1:
        lower_square = math.floor(v)
        upper_square = math.floor(v)+2
    else:
        lower_square = math.floor(v)-1
        upper_square = math.floor(v)+1
    n = (lower_square + 1) // 2
    amount = 8 * (n-1)
    if side == "left":
        return k - (amount + 5)
    if side == "right":
        return k - (amount + 1)
    if side == "top":
        return k - (amount + 3)
    return k - (amount + 7)

def get_steps(k):
    if k == 1:
        return 0
    if is_plus(k):
        return is_plus(k)
    if is_diag(k):
        return is_diag(k)
    side = get_side(k) #top/bottom/left/right (can't be corner)
    steps = 0
    while (not is_plus(k)) and (not is_diag(k)):
        k = take_step(k, side)
        steps += 1
    if is_plus(k):
        return steps + is_plus(k)
    else:
        return steps + is_diag(k)

def make_grid():
    INPUT = 368078
    grid = [[0 for i in range(10)] for j in range(10)]
    last = 1
    grid[4][4] = 1
    #got lazy
    print(grid)
