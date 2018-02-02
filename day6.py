'''
16 banks
each bank holds unlimited blocks
goal to balance blocks between banks

in cycles:
finds bank with most (ties won by lowest-numbered), redistributes by:
    remove all from selected bank
    move to next bank by index and insert one
    continue until out
    wrap to first after last

question:
    how many redistributions can be done before a blocks-in-banks config is
    produced that has been seen before?
'''

TEST_BANKS = [0,2,7,0]
BANKS = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]

def get_redist(banks):
    idx = banks.index(max(banks))
    n = banks[idx]
    banks[idx] = 0
    while n > 0:
        idx = (idx + 1) % len(banks)
        banks[idx] += 1
        n -= 1
    return banks

def count_redists(banks):
    count = 0
    seen = set()
    t = tuple(banks)
    seen.add(t)
    while True:
        count += 1
        banks = get_redist(banks)
        #print(banks)
        t = tuple(banks)
        if t in seen:
            return count
        seen.add(t)

def count_loop_length(banks):
    seen = [banks.copy()]
    while True:
        banks = get_redist(banks)
        #print(banks)
        if banks in seen:
            return len(seen) - seen.index(banks)
        seen.append(banks.copy())
