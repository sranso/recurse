#!/usr/bin/env python3

import pdb
import copy

# BASIC KOSARAJU ALGORITHM
# grev = g with all arcs reversed
# run dfs-loop on grev
#   compute 'magical order' of nodes
# run dfs loop on g
#   discover sccs(nodes w same 'leader') one-by-one


graph = {
    # value: (visited, [arcs])
    1: (False, set([3])),
    2: (False, set([1, 4])),
    3: (False, set([2, 5])),
    4: (False, set([6])),
    5: (False, set([4])),
    6: (False, set([5])),
}

graphrev = {
    # value: (visited, [arcs])
    1: (False, set([2])),
    2: (False, set([3])),
    3: (False, set([1])),
    4: (False, set([2, 5])),
    5: (False, set([6, 3])),
    6: (False, set([4])),
}

graph_rev = {}
def dfs_loop_graphr(graph_orig, startvertex):
    if not startvertex in graph_rev:
        graph_rev[startvertex] = (False, [])
    for edge in graph_orig[startvertex][1]:
        print edge, startvertex, graph_rev
        if edge in graph_rev:
            graph_rev[edge][1].append(startvertex)
            if graph_rev[edge][0]:
                return
        else:
            graph_rev[edge] = (False, [startvertex])
        graph_rev[edge] = (True, graph_rev[edge][1])
        dfs_loop_graphr(graph_orig, edge)

def dfs_loop(graph, startvertex):
    graph[startvertex] = (True, graph[startvertex][1])
    for edge in graph[startvertex][1]:
        if not graph[edge][0]:
            dfs_loop(graph, edge)

print dfs_loop_graphr(graph, 1)
print graph_rev







#with open('./data.txt') as f:
#    for line in f:
#        # do stuff

