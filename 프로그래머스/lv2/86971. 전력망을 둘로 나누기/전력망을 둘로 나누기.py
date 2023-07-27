from copy import deepcopy
from collections import deque, defaultdict

def make_tree(wires):
    visited,tree = set(), defaultdict(set)
    for wire in wires:
        tree[wire[0]].add(wire[1])
        tree[wire[1]].add(wire[0])
    return tree

def nodes_1(tree):
    visited = set()
    nodes = deque([1])
    while nodes :
        node = nodes.pop()
        if node in visited : continue
        nodes.extend(list(tree[node]))
        visited.add(node)
        #print(node)
        
    return len(visited)


def solution(n, wires):
    answer = []
    tree = make_tree(wires)
    for cut in wires:
        cutted_tree = deepcopy(tree)
        cutted_tree[cut[0]].remove(cut[1])
        cutted_tree[cut[1]].remove(cut[0])
        #print(cut, cutted_tree)
        ans = abs(2*nodes_1(cutted_tree)-n)
        if ans == 0 : return 0
        else : answer.append(ans)
    return min(answer)