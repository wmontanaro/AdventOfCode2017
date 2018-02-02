FNAME = "day9.txt"

def get_data(file):
    with open(file, "r") as f:
        s = [l.strip() for l in f.readlines()][0]
    return s

def get_score(s):
    score = 0
    cur_level = 0
    #stack = []
    idx = 0
    in_garbage = False
    l = list(s)
    while idx < len(l):
        char = l[idx]
        idx += 1
        if char == "!":
            idx += 1
            continue
        if in_garbage:
            if char == ">":
                in_garbage = False
            continue
        if char == "<":
            in_garbage = True
            continue
        if char == "{":
            cur_level += 1
            continue
        if char == "}":
            score += cur_level
            cur_level -= 1
            continue
        else:
            continue
    return score
        
def get_garbage(s):
    score = 0
    #cur_level = 0
    #stack = []
    idx = 0
    in_garbage = False
    l = list(s)
    while idx < len(l):
        char = l[idx]
        idx += 1
        if char == "!":
            idx += 1
            continue
        if in_garbage:
            if char == ">":
                in_garbage = False
            else:
                score += 1
            continue
        if char == "<":
            in_garbage = True
            continue
        #if char == "{":
            #cur_level += 1
            #continue
        #if char == "}":
            #score += cur_level
            #cur_level -= 1
            #continue
        else:
            continue
    return score
