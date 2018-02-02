FNAME = "day12.txt"

def get_data(file):
    with open(file, "r") as f:
        d = [line.strip() for line in f.readlines()]
    return d

def get_dict(data):
    d = dict()
    s = [item.replace(",", "") for item in data]
    s = [item.split(" ") for item in s]
    for item in s:
        item.pop(1)
    for item in s:
        d[item[0]] = item[1:]
    return d

def get_containing_set(d, node):
    #d = get_dict(data)
    container = set([node])
    to_check = d[node]
    checked = set([node])
    while len(to_check) > 0:
        checking = to_check.pop()
        container.add(checking)
        for n in d[checking]:
            if n not in to_check and n not in checked:
                to_check.append(n)
        checked.add(checking)
    return container
    #return len(container)

def get_all_groups(data):
    d = get_dict(data)
    checked = set()
    groups = []
    for node in d:
        if node not in checked:
            group = get_containing_set(d, node)
            groups.append(group)
            checked = checked.union(set(group))
    return len(groups)
