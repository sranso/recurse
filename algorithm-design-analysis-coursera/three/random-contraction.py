#!/usr/bin/env python

import pprint
import pdb
import random
import copy


#     A ----- B            .---- B
#     |     / |   A,C     /    / |
#     | .--'  | ------> AC ---'  |
#     |/      |           \      |
#     C ----- D            `---- D

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"],

    #("A", "B"): ["C", "C", "D"]
}


# sarah's algorithm
#   pick vertex and one of its edges
#   insert the tuple into the dict,
#       mapped to the union of the edges of the two chosen verticies
#   iterate through that list:
#       remove verticies which correspond to chosen item (drop loopback edges)
#       recurse into items, updating references of self to new tuple
#   repeat until only two entries in dict

def mincut(graph):
    while len(graph.keys()) > 2:

        vert = random.choice(graph.keys())
        othervert = graph[vert][random.randint(0, len(graph[vert]) - 1)]
        edge = (vert, othervert)


        _list = []
        for _vert in graph[vert] + graph[othervert]:
            if _vert not in [vert, othervert]:
                _list.append(_vert)

        graph[edge] = _list
        for _vert in _list:
            for i, __vert in enumerate(graph[_vert]):
                if __vert in [vert, othervert]:
                    graph[_vert][i] = edge

        del graph[vert]
        del graph[othervert]



    return len(graph[random.choice(graph.keys())])

graph = {}
with open('./graph.in', 'r') as f:
    for line in f.readlines():
        cols = line.strip().split()
        graph[cols[0]] = cols[1:]

#p = pprint.PrettyPrinter(width=1, indent=2)
#p.pprint(graph)

min = -1
for i in range(0, 10):
    t = mincut(copy.deepcopy(graph))
    print t
    if t < min or min == -1:
        min = t

print "answer: ", min
