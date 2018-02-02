import collections

TESTFNAME = "day7test.txt"
FNAME = "day7.txt"

def get_trees(file):
    with open(file, "r") as f:
        rawdata = [line.strip() for line in f.readlines()]
    splitdata = [line.split(" ") for line in rawdata]
    tree = dict() #{[entry : [children]}
    revtree = dict() #{entry : parent}
    weights = dict() #{entry : weight}
    for item in splitdata:
        weights[item[0]] = int(item[1].replace("(", "").replace(")", ""))
        children = [entry.replace(",", "") for entry in item[3:]]
        tree[item[0]] = children
        for child in children:
            revtree[child] = item[0]
    return (tree, revtree, weights)

def get_root(file):
    trees = get_trees(file)
    root = [item for item in trees[0] if item not in trees[1]][0]
    return root

def get_subtower_nodes(node, tree):
    #includes all subtowers and the node itself
    nodes = [node]
    children = [item for item in tree[node]]
    while len(children) > 0:
        child = children.pop()
        nodes.append(child)
        children += tree[child]
    return nodes

def get_total_weight(subtower, weights):
    total = 0
    for node in subtower:
        total += weights[node]
    return total

def find_unbalanced_node(file):
    root = get_root(file)
    trees = get_trees(file)
    tree = trees[0]
    revtree = trees[1]
    weights = trees[2]
    for node in tree:
        child_weights = dict()
        children = tree[node]
        for child in children:
            child_weight = get_total_weight(
                get_subtower_nodes(child, tree),
                weights)
            child_weights[child] = child_weight
        if len(set(child_weights.values())) > 1:
            l = list(child_weights.values())
            l.sort()
            if l.count(l[0]) == 1:
                weird_weight = l[0]
                normal_weight = l[-1]
            else:
                weird_weight = l[-1]
                normal_weight = l[0]
            #print(child_weights)
            #print(weights[child])
            #print(weird_weight)
            #print(normal_weight)
            for kid in child_weights:
                if child_weights[kid] == weird_weight:
                    weird_node = kid
            #print(weird_node)
            #print(weights[weird_node])
            return weights[weird_node] - (weird_weight - normal_weight)
