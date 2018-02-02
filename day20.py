FILE = "day20.txt"
TFILE = "day20test.txt"

def get_nums(sline_piece):
    raw = sline_piece[3:-1]
    split = raw.split(",")
    nums = [int(item) for item in split]
    return nums

def get_data(file):
    with open(file, "r") as f:
        raw = [line.strip() for line in f.readlines()]
    data = []
    for line in raw:
        sline = line.split(", ")
        p = get_nums(sline[0])
        v = get_nums(sline[1])
        a = get_nums(sline[2])
        data.append({'p': p, 'v': v, 'a': a})
    return data

def step(data):
    for i in range(len(data)):
        for j in range(3):
            data[i]['v'][j] += data[i]['a'][j]
            data[i]['p'][j] += data[i]['v'][j]
    #return data

def manstuff(particles):
    mandists = [
        sum
        ([abs(item) for item in particle['p']])
        for particle in particles]
    mindist = min(mandists)
    minind = mandists.index(mindist)
    mindiffs = [item - mindist for item in mandists]
    return(minind, mindiffs)

def zbuff(file):
    particles = get_data(file)
    numparts = len(particles)
    minind, mindiffs = manstuff(particles)
    while True:
        for i in range(1000):
            step(particles)
        #print('particles: ' + str(particles))
        print(minind)
        newminind, newmindiffs = manstuff(particles)
        if minind == newminind:
            diffstate = True
            for i in range(numparts):
                if newmindiffs[i] < mindiffs[i]:
                    diffstate = False
                    break
            if diffstate:
                return minind
        minind = newminind
        mindiffs = newmindiffs

#-------------------------------------------------------------#
'''
t = 0:
partApos = p
t = 1:
partApos = p + (v + a)
t = 2:
partApos = p + (v+a) + (v+a+a) = p + 2v + 3a
t = 3:
partApos = p + (v+a) + (v+a+a) + (v+a+a+a) = p + 3v + 6a
p(t) = p(0) + vt + (t*(t+1)/2)*a

so if there is some t such that partApos = partBpos for x,y,z, then they will
collide. this is not useful for predicting collisions; after all, if a and b
might collide, a and c might collide first.

However, it gives another way to do the 'step' step, if desired.
'''

'''
find overlapping positions
make new list with only non-overlappers
step
check if all distances between all objects are nonincreasing
repeat
'''

def get_col_data(file):
    with open(file, "r") as f:
        raw = [line.strip() for line in f.readlines()]
    data = []
    for i in range(len(raw)):
        line = raw[i]
        sline = line.split(", ")
        p = get_nums(sline[0])
        v = get_nums(sline[1])
        a = get_nums(sline[2])
        data.append({'p': p, 'v': v, 'a': a})
    return data

def clean_cols(particles):
    pass



def collide(file):
    particles = get_col_data(file)
    to_remove = []
    
