FNAME = "day16.txt"
TFILE = "day16test.txt"
PROGRAMS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
TPROGRAMS = ['a', 'b', 'c', 'd', 'e']

def get_data(file):
    with open(file, "r") as f:
        d = [line.strip() for line in f.readlines()]
    s = d[0].split(",")
    return s

def spin(x, programs):
    new_programs = programs[-x:] + programs[:-x]
    return new_programs

def exchange(a, b, programs):
    new_programs = programs
    new_programs[a], new_programs[b] = programs[b], programs[a]
    return new_programs

def partner(a, b, programs):
    aind = programs.index(a)
    bind = programs.index(b)
    new_programs = programs
    new_programs[aind], new_programs[bind] = programs[bind], programs[aind]
    return new_programs

def dance(file, programs):
    s = get_data(file)
    for op in s:
        if op[0] == "s":
            programs = spin(int(op[1:]), programs)
        elif op[0] == "x":
            sop = op.split("/")
            sop[0] = sop[0][1:]
            programs = exchange(int(sop[0]), int(sop[1]), programs)
        elif op[0] == "p":
            programs = partner(op[1], op[3], programs)
    return "".join(programs)

import copy

def get_partner_steps(steps):
    partner_steps = [op for op in steps if op[0] == "p"]

def get_perm(s, programs):
    tprograms = copy.deepcopy(programs)
    for op in s:
        if op[0] == "s":
            tprograms = spin(int(op[1:]), tprograms)
        elif op[0] == "x":
            sop = op.split("/")
            sop[0] = sop[0][1:]
            tprograms = exchange(int(sop[0]), int(sop[1]), tprograms)
        #elif op[0] == "p":
            #programs = partner(op[1], op[3], programs)
    perm = [tprograms.index(programs[i]) for i in range(len(programs))]
    return perm

def do_perm(programs, perm):
    new_programs = [None for i in range(len(perm))]
    for i in range(len(perm)):
        new_programs[perm[i]] = programs[i]
    return new_programs

def get_cycle_length(programs, perm):
    tprograms = copy.deepcopy(programs)
    counter = 0
    while True:
        counter += 1
        tprograms = do_perm(tprograms, perm)
        if tprograms == programs:
            return counter

def full_dance(file, programs, n):
    steps = get_data(file)
    if n % 2 != 0:
        partner_steps = get_partner_steps(steps)
        for op in partner_steps:
            programs = partner(op[1], op[3], programs)
    perm = get_perm(steps, copy.deepcopy(programs))
    cycle_length = get_cycle_length(programs, perm)
    for i in range(n % cycle_length):
        programs = do_perm(programs, perm)
    return "".join(programs)
