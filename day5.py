FILE = "day5.txt"

def get_data(fname):
    with open(fname, "r") as f:
        d = [int(l.strip()) for l in f.readlines()]
    return d

def count_steps(fname):
    d = get_data(fname)
    count = idx = 0
    while idx in range(0, len(d)):
        count += 1
        old_val = d[idx]
        d[idx] += 1
        idx += old_val
    return count

def count_more_steps(fname):
    d = get_data(fname)
    count = idx = 0
    while idx in range(0, len(d)):
        count += 1
        old_val = d[idx]
        if old_val > 2:
            d[idx] -= 1
        else:
            d[idx] += 1
        idx += old_val
    return count
