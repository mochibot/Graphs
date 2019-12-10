from util import Stack

def get_parents(ancestors, starting_node):
    parents = set()
    for item in ancestors:
        if item[1] == starting_node:
            parents.add(item[0])
    return parents

'''
first pass solution - using DFS
from starting_node, check if there is parent and traverse through the graphs
initial result variable to -1. update with value of the parent
if multiple parents, pick the smaller one
get_parents method returns a set of parents for the starting_node
'''

def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push(starting_node)
    visited = set()
    result = -1
    parents = []
    while s.size() > 0:
        node = s.pop()
        if node not in visited:
            visited.add(node)
            if len(parents) > 0:
                result = min(parents)
            parents = []
            for parent in get_parents(ancestors, node):
                s.push(parent)
                parents.append(parent)
    return result

if __name__ == '__main__':
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(get_parents(ancestors, 1))
    print(earliest_ancestor(ancestors, 6))
    print(earliest_ancestor(ancestors, 9))
    print(earliest_ancestor(ancestors, 7))
    print(earliest_ancestor(ancestors, 2))
