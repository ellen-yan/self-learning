# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 1, Part 3 of 3
#
# Supplemental: testing whether file has multiple edges per any pair of nodes

import fileinput
import math

def read_from_file(filename):
    """Test whether any pair of nodes contain more than one edge"""
    
    edge_set = set()

    i = 0
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) != 2:
            x = int(l[0])
            y = int(l[1])
            if x == y:
                print("found selfloop:", x)
            
            if (x,y) not in edge_set and (y,x) not in edge_set:
                edge_set.add((x,y))
            else:
                print ("repeated edge at:", x, y)
    return edge_set

edge_set = read_from_file("edges.txt")

print("done")
