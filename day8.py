TFILE = "day8test.txt"
FILE = "day8.txt"

def gt(a, b):
    if a > b:
        return True
    return False

def lt(a, b):
    if a < b:
        return True
    return False

def gte(a, b):
    if a >= b:
        return True
    return False

def lte(a, b):
    if a <= b:
        return True
    return False

def eq(a, b):
    if a == b:
        return True
    return False

def neq(a, b):
    if a != b:
        return True
    return False

def find_highest_register(file):
    with open(file, "r") as f:
        data = [line.strip() for line in f.readlines()]
    registers = {}
    COMPARISONS = {">": gt, "<": lt, ">=": gte, "<=": lte, "==": eq, "!=": neq}
    highest = 0
    for line in data:
        sline = line.split(" ")
        compreg = sline[4]
        condop = sline[5]
        compamount = int(sline[6])
        if compreg not in registers:
            registers[compreg] = 0
        if COMPARISONS[condop](registers[compreg], compamount):
            insreg = sline[0]
            insop = sline[1]
            insamount = int(sline[2])
            if insreg not in registers:
                registers[insreg] = 0
            if insop == "inc":
                registers[insreg] += insamount
            else:
                registers[insreg] -= insamount
            if registers[insreg] > highest:
                highest = registers[insreg]
    return highest
    #return max(registers.values())
