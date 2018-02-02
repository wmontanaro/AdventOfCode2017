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
    if k == 1:
        return 0
    if is_down(k):
        return is_down(k)
    if is_right(k):
        return is_right(k)
    if is_left(k):
        return is_left(k)
    if is_up(k):
        return is_up(k)
    return False

'''figure out if up or down, move opposite to plus'''
'''how to figure out if up or down?

can figure out its octant by starting with the floor of its square root
e.g. 18 lies between upper left diag (n=2) and left plus
e.g. 47 -> 6, n=3; so UL is 37, L is 40, LL is 43, D is 46, D+1 is 47

so to summarize up/down:
floor sqrt // 2 -> n
(368078 -> 303)
this is the ring the number is on
if (2n)**2 + 1 <= num < (2n)**2 + 1 + n, then it is up
if (2n)**2 + 1 + n < num < (2n)**2'''

import math

def check_square(k):
    v = math.sqrt(k)
    if int(v) == v: #v perfect square
        return(int(v)-1)
    return False

def get_vert(k):
    #if check_square(k):
        #return "square"
    v = math.sqrt(k)
    if math.floor(v) % 2 == 1:
        lower_square = math.floor(v)
        upper_square = math.floor(v)+2
    else:
        lower_square = math.floor(v)-1
        upper_square = math.floor(v)+1
    #print("lower_square: " + str(lower_square))
    #print("upper_square: " + str(upper_square))
    n = (lower_square + 1) // 2
    #print("n: " + str(n))
    left = 4*(n**2) + 1 + n
    #print("left: " + str(left))
    right = 4*(n**2) + 1 - (3*n)
    #print("right: " + str(right))
    if right < k < left:
        return "above 1"
    return "below 1"

def step_down(k):
    pass

def tfunc(k):
    if is_plus(k):
        return is_plus(k)
    vert = get_vert(k)
    steps = 0
    if vert == "above 1":
        while not is_plus(k):
            k = step_down(k)
            steps += 1
        return steps + is_plus(k)
    if vert == "below 1":
        while not is_plus(k):
            k = step_up(k)
            steps += 1
    
