FILE = "day4.txt"

def get_data(fname):
    with open(fname, "r") as f:
        d = [l.strip() for l in f.readlines()]
    return d

def check_line(line):
    sline = line.split(" ")
    if len(set(sline)) == len(sline):
        return True
    return False

def get_valid_count(fname):
    data = get_data(fname)
    count = 0
    for line in data:
        if check_line(line):
            count += 1
    return count

import itertools

def check_anagram(word1, word2):
    word1grams = set(itertools.permutations(word1))
    if tuple(word2) in word1grams:
        return True
    return False

def check_gram_line(line):
    sline = line.split(" ")
    for i in range(len(sline)-1):
        for j in range(i+1, len(sline)):
            if check_anagram(sline[i], sline[j]):
                return False
    return True

def get_valid_gram_count(fname):
    data = get_data(fname)
    count = 0
    for line in data:
        if check_gram_line(line):
            count += 1
    return count
