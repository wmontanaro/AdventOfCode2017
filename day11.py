FNAME = "day11.txt"

def get_data(file):
    with open(file, "r") as f:
        raw = [l.strip() for l in f.readlines()][0]
    s = raw.split(",")
    return s

'''
n and s
ne and sw
nw and se

combinations:
n, ne, nw -> ne + nw = n, left with n and ne/nw
n, ne, se -> n + se = ne, left with ne and n/se
n, sw, nw -> n + sw = nw, left with nw and n/sw
n, sw, se -> harder
s, ne, nw -> harder
s, ne, se -> ne + s = se, left with se and ne/s
s, sw, nw -> s + nw = sw, left with sw and s/nw
s, sw, se -> sw + se = s, left with s and sw/se

n, sw, se:
n + sw = ne, left with n, ne, se (above) or sw, ne, se (ne/sw cancel)
n + sw + se = 0

s, ne, nw:
s + ne = sw, left with s, sw, nw (above) or ne, sw, nw (ne/sw cancel)


a + b + c = 0
a < b < c
0 < b-a < c-a
-(b-a) < 0 < c-a-b+a = c-b
'''


def reduce(a, b):
    if a > b:
        return (a-b, 0)
    else:
        return (0, b-a)

def case_s_ne_nw(s, ne, nw):
    #min of these cancels out; if s, left with ne, nw
    #ne + nw = n, so min is n, with max - min leftover
    #say ne > nw; n = nw, ne = ne - nw
    #take n + ne = nw + ne - nw = ne steps
    #so should be max - min
    return max(s, ne, nw) - min(s, ne, nw)

def case_n_sw_se(n, sw, se):
    return max(n, sw, se) - min(n, sw, se)

def get_steps(steps):
    n = steps.count("n")
    ne = steps.count("ne")
    se = steps.count("se")
    s = steps.count("s")
    sw = steps.count("sw")
    nw = steps.count("nw")
    n, s = reduce(n, s)
    ne, sw = reduce(ne, sw)
    nw, se = reduce(nw, se)
    if n == 0: #s
        if ne == 0: #sw
            if nw == 0: #se
                return s + max(sw, se)
            else: #nw
                return sw + max(s, nw)
        else: #ne
            if nw == 0: #se
                return se + max(ne, s)
            else: #nw
                return case_s_ne_nw(s, ne, nw)
    else: #n
        if ne == 0: #sw
            if nw == 0: #se
                return case_n_sw_se(n, sw, se)
            else: #nw
                return nw + max(n, sw)
        else: #ne
            if nw == 0: #se
                return ne + max(n, se)
            else: #nw
                return n + max(ne, nw)
    
def get_farthest(steps):
    highest = 0
    for i in range(len(steps)):
        dist = get_steps(steps[:i])
        if dist > highest:
            highest = dist
    return highest
