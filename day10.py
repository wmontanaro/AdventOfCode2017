LENGHTS = [106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36]
RING = list(range(256))

TEST_LENGTHS = [3,4,1,5]
TEST_RING = list(range(5))

def customHash(lengths, ring):
    rlen = len(ring)
    idx = 0
    skip_size = 0
    for length in lengths:
        #print("processing length " + str(length))
        if length > rlen:
            continue
        to_rev = []
        tempidx = 0
        #print("getting to_rev")
        while tempidx < length:
            #print("tempidx = " + str(tempidx))
            to_rev.append(ring[(idx + tempidx) % rlen])
            #print("to_rev = " + str(to_rev))
            tempidx += 1
        tempidx = 0
        #print("updating ring")
        while tempidx < length:
            ring[(idx + tempidx) % rlen] = to_rev.pop()
            tempidx += 1
        idx += length
        idx += skip_size
        idx = idx % rlen
        skip_size += 1
    return ring[0] * ring[1]

'''
treat input as string
convert input to ascii code via ord(char)
run 64 rounds, carrying over position and skip size
reduce sparse to dense - XOR 16 at a time via a1^a2....
convert dense to hex via hex(n), then format (it's a string)
'''

S = "106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36"

def customRound(lengths, ring, skip_size, idx):
    rlen = len(ring)
    for length in lengths:
        if length > rlen:
            continue
        to_rev = []
        tempidx = 0
        while tempidx < length:
            to_rev.append(ring[(idx + tempidx) % rlen])
            tempidx += 1
        tempidx = 0
        while tempidx < length:
            ring[(idx + tempidx) % rlen] = to_rev.pop()
            tempidx += 1
        idx += length
        idx += skip_size
        idx = idx % rlen
        skip_size += 1
    return (ring, skip_size, idx)

def get_dense(ring):
    denseHash = []
    idx = 0
    while idx <= len(ring) - 16:
        count = 0
        for item in ring[idx:idx+16]:
            count ^= item
        denseHash.append(count)
        idx += 16
    return denseHash

def get_hex(denseHash):
    s = ""
    for val in denseHash:
        h = hex(val)[2:]
        s += '{:0>2}'.format(h)
    return s

def fullHash(lengths, ring):
    clengths = []
    for char in lengths:
        clengths.append(ord(char))
    EXTRA = [17, 31, 73, 47, 23]
    clengths += EXTRA
    skip_size = 0
    idx = 0
    for i in range(64):
        r = customRound(clengths, ring, skip_size, idx)
        ring, skip_size, idx = r
    denseHash = get_dense(ring)
    hexHash = get_hex(denseHash)
    return hexHash
    
