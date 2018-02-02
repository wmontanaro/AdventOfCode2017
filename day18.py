FILE = "day18.txt"
TFILE = "day18test.txt"

REGS = dict()

def get_ins(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def parse_ins(line, registers):
    sline = line.split(" ")
    ins = sline[0]
    reg = sline[1]
    try:
        val = int(sline[2])
    except ValueError:
        val = registers[sline[2]]
    except IndexError:
        val = None
    return (ins, reg, val)

def get_rvc(file, regs):
    registers = REGS
    lines = get_ins(file)
    last_sound = None
    idx = 0
    while idx in range(len(lines)):
        ins, reg, val = parse_ins(lines[idx], registers)
        if reg not in registers:
            registers[reg] = 0
        if ins == "snd":
            last_sound = registers[reg]
            idx += 1
        elif ins == "set":
            registers[reg] = val
            idx += 1
        elif ins == "add":
            registers[reg] += val
            idx += 1
        elif ins == "mul":
            try:
                registers[reg] *= val
                idx += 1
            except TypeError:
                return
        elif ins == "mod":
            registers[reg] = registers[reg] % val
            idx += 1
        elif ins == "rcv":
            if registers[reg] == 0:
                idx += 1
            else:
                return last_sound
        elif ins == "jgz":
            if registers[reg] > 0:
                idx += val
            else:
                idx += 1
                

#------------------------------------------------------#

def one_time_parse(lines):
    instructions = []
    for line in lines:
        sline = line.split(" ")
        ins = sline[0]
        reg = sline[1]
        try:
            val = sline[2]
        except IndexError:
            val = None
        instructions.append((ins, reg, val))
    return instructions

def do_work(instructions, regs, idx, inqueue, outqueue):
    numsends = 0
    while idx in range(len(instructions)):
        ins, reg, val = instructions[idx]
        try:
            val = int(val)
        except ValueError:
            val = regs[val]
        except TypeError:
            #print(instructions[idx])
            #print(regs)
            #print(idx)
            #print(ins)
            #print(reg)
            #print(val)
            #print(outqueue)
            val = None
        if reg not in regs and reg != "1":
            regs[reg] = 0
        if ins == "snd":
            outqueue.append(regs[reg])
            numsends += 1
            idx += 1
        elif ins == "set":
            regs[reg] = val
            idx += 1
        elif ins == "add":
            regs[reg] += val
            idx += 1
        elif ins == "mul":
            regs[reg] *= val
            idx += 1
        elif ins == "mod":
            regs[reg] = regs[reg] % val
            idx += 1
        elif ins == "rcv":
            if len(inqueue) > 0:
                regs[reg] = inqueue.pop(0)
                idx += 1
            else:
                return(regs, idx, inqueue, outqueue, numsends)
        elif ins == "jgz":
            if reg == "1" or regs[reg] > 0:
                idx += val
            else:
                idx += 1
    print("out of range")

def messaging(file):
    lines = get_ins(file)
    instructions = one_time_parse(lines)
    reg0 = {"p": 0}
    reg1 = {"p": 1}
    to1 = []
    to0 = []
    count = 0
    idx0 = 0
    idx1 = 0
    while True:
        reg0, idx0, to0, to1, numsends = \
              do_work(instructions, reg0, idx0, to0, to1)
        reg1, idx1, to1, to0, numsends = \
              do_work(instructions, reg1, idx1, to1, to0)
        count += numsends
        if len(to0) == 0 and len(to1) == 0:
            return count
