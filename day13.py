FNAME = "day13.txt"
TDATA = "day13test.txt"

def get_data(file):
    with open(file, "r") as f:
        d = [line.strip() for line in f.readlines()]
    return d

def get_initial_state(data):
    state = dict() #{layer : [range, position, direction]}
    d = [line.split(": ") for line in data]
    for layer in d:
        state[int(layer[0])] = [int(layer[1])-1, 0, "up"]
        #note -1 because range of 3 means highest index is 2
    return state

def advance_state(state):
    for layer in state:
        r = state[layer][0]
        pos = state[layer][1]
        direction = state[layer][2]
        #position = 0, position = range, direction = 'up', direction ='down'
        if pos == 0:
            state[layer][1] = 1
            state[layer][2] = "up"
        elif pos == r:
            state[layer][1] = r-1
            state[layer][2] = "down"
        else: #between 0 and r
            if direction == "up":
                state[layer][1] = pos + 1
            else:
                state[layer][1] = pos - 1
    return state

def get_severity(file):
    d = get_data(file)
    state = get_initial_state(d)
    curpos = 0
    severity = 0
    while curpos < max(state):
        state = advance_state(state)
        #print('state: ' + str(state))
        curpos += 1
        #print('curpos: ' + str(curpos))
        if curpos in state:
            #print('guard on duty')
            if state[curpos][1] == 0:
                #print('guard at top')
                severity += curpos * (state[curpos][0] + 1)
                #print('severity now ' + str(severity))
    return severity

import copy
    
def sneak(file):
    d = get_data(file)
    delay = 0
    ini_state = get_initial_state(d)
    while True:
        #if delay > 15:
            #return 'no'
        delay += 1
        state = copy.deepcopy(ini_state)
        ini_state = advance_state(ini_state)
        curpos = -1
        caught = False
        while curpos < max(state):
            curpos += 1
            state = advance_state(state)
            if curpos in state:
                if state[curpos][1] == 0:
                    caught = True
                    break
        if caught == False:
            return delay

def is_caught(delay, condition):
    if (delay + condition[0]) % condition[1] == 0:
        return True
    return False

def crtlike(file):
    d = get_data(file)
    s = get_initial_state(d)
    delay = 0
    conditions = []
    for item in s:
        offset = item
        multiple = 2 * s[item][0]
        conditions.append((offset, multiple))
    #print(conditions)
    while True:
        delay += 1
        caught = False
        for condition in conditions:
            if is_caught(delay, condition):
                caught = True
                break
        if caught == False:
            return delay
