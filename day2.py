FNAME = "day2.txt"

def get_rows(FNAME):
    with open(FNAME, "r") as f:
        raw_data = [l.strip() for l in f.readlines()]
    split_data = [l.split("\t") for l in raw_data]
    num_data = [[int(item) for item in line] for line in split_data]
    return num_data

def get_checksum(num_data):
    tot = 0
    for row in num_data:
        tot += max(row) - min(row)
    return tot

def even_div(row):
    for i in range(len(row)-1):
        for j in range(i+1, len(row)):
            if int(row[i]/row[j]) == row[i]/row[j]:
                return int(row[i]/row[j])
            elif int(row[j]/row[i]) == row[j]/row[i]:
                return int(row[j]/row[i])

def adv_get_checksum(num_data):
    tot = 0
    for row in num_data:
        tot += even_div(row)
    return tot
