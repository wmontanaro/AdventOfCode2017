FILE = "day19.txt"
TFILE = "day19test.txt"

def get_maze(file):
    with open(file, "r") as f:
        maze = [line.replace("\n", "") for line in f.readlines()]
    return maze

def get_word(file):
    maze = get_maze(file)
    x = maze[0].index("|")
    y = 0
    #curpos = [maze[0].index("|"), 0]
    #xrange = list(range(len(maze[0])))
    #yrange = list(range(len(maze)))
    #xmax = len(maze[0])
    #ymax = len(maze)
    direction = "down"
    word = ""
    steps = 0
    while True:
        steps += 1
        if direction == "down":
            y += 1
        elif direction == "left":
            x += -1
        elif direction == "right":
            x += 1
        elif direction == "up":
            y += -1
        curitem = maze[y][x]
        if curitem == "+":
            #get new direction
            if direction in ["down", "up"]:
                if x-1 < 0 or maze[y][x-1] == " ":
                    direction = "right"
                else:
                    direction = "left"
            elif direction in ["left", "right"]:
                if y-1 < 0 or maze[y-1][x] == " ":
                    direction = "down"
                else:
                    direction = "up"
##            elif direction == "right":
##                if y-1 < 0 or maze[y-1][x] == " ":
##                    direction = "down"
##                else:
##                    direction = "up"
##            elif direction == "up":
##                if x-1 < 0 or maze[y][x-1] == " ":
##                    direction = "right"
##                else:
##                    direction = "left"
        elif curitem in ["|", "-"]:
            #do nothing, must be in same direction
            pass
        elif curitem == " ":
            #off the path, done
            #return word
            return steps
        else:
            word += curitem
