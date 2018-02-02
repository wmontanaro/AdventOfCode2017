VAL = 369
TVAL = 3
INSERTS = 2017
TINSERTS = 10

def spinlock(step_size, inserts):
    buffer = [0]
    curval = 0
    curpos = 0
    while curval < inserts:
        curval += 1
        #print("curval: " + str(curval))
        newpos = (curpos + step_size) % len(buffer)
        #print("newpos: " + str(newpos))
        buffer.insert(newpos+1, curval)
        #print(buffer)
        curpos = newpos + 1
    return buffer[buffer.index(2017)+1]

FASTERINSERTS = 50000000

def faster_spinlock(step_size, inserts):
    buffer = [0]
    curval = 0
    curpos = 0
    while curval < inserts:
        curval += 1
        #print("curval: " + str(curval))
        newpos = (curpos + step_size) % len(buffer)
        #print("newpos: " + str(newpos))
        buffer.insert(newpos+1, curval)
        #print(buffer)
        curpos = newpos + 1
    return buffer[buffer.index(0)+1]

'''
don't care about nonzero values except the one after zero; we can ignore
the rest of the buffer as we only care about the length
'''

def faster_spinlock2(step_size, inserts):
    buffer_size = 1
    curval = 0
    curpos = 0
    after_zero = None
    while curval < inserts:
        if curval % 1000000 == 0:
            print("working on " + str(curval))
        curval += 1
        #print("curval: " + str(curval))
        newpos = (curpos + step_size) % buffer_size
        #print("newpos: " + str(newpos))
        buffer_size += 1
        #print("buffer_size: " + str(buffer_size))
        if newpos == 0:
            after_zero = curval
            #print(str(after_zero))
        curpos = newpos + 1
        #print("curpos: " + str(curpos))
    return after_zero
