ASEED = 703
BSEED = 516
AFACTOR = 16807
BFACTOR = 48271
ATESTSEED = 65
BTESTSEED = 8921
DIVISOR = 2147483647

def get_next_value(cur_val, factor):
    next_val = (cur_val * factor) % DIVISOR
    return next_val

def compare(valA, valB):
    sa = bin(valA)[-16:]
    sb = bin(valB)[-16:]
    if sa == sb:
        return True
    return False

def judge(aval, bval, n):
    matches = 0
    for i in range(n):
        aval = get_next_value(aval, AFACTOR)
        bval = get_next_value(bval, BFACTOR)
        if compare(aval, bval):
            matches += 1
    return matches

def adv_judge(aval, bval, n):
    matches = 0
    for i in range(n):
        aval = get_next_value(aval, AFACTOR)
        while aval % 4 != 0:
            aval = get_next_value(aval, AFACTOR)
        bval = get_next_value(bval, BFACTOR)
        while bval % 8 != 0:
            bval = get_next_value(bval, BFACTOR)
        if compare(aval, bval):
            matches += 1
    return matches
        
