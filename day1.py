def checksum(seq):
    tot = 0
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            tot += int(seq[i])
    if len(seq) > 1:
        if seq[0] == seq[-1]:
            tot += int(seq[0])
    return tot

def adv_checksum(seq):
    tot = 0
    l = len(seq)
    step = int(l/2)
    for i in range(l):
        comp_idx = (i + step) % l
        if seq[i] == seq[comp_idx]:
            tot += int(seq[i])
    return tot
