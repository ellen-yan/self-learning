# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 1, Part 3 of 3
#
# Given a graph, run Prim's minimum spanning tree algorithm on the graph
# and report the overall cost of a minimum spanning tree (an integer which
# may or may not be negative). There is at most one edge per pair of nodes
# and there are no self loops.

import fileinput

def read_from_file(filename):
    """For Part 3: Reads a file containing a graph with the input per line:
    node node edge_cost, and returns the vertices and edges of the graph and
    assigns a key to each node assuming the source node is 1"""
    
    edges_dict = {} # maps the tuple of vertices to the weight of the edge
    v_set = set() # set of all vertices
    
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        
        if len(l) != 2:
            node1 = int(l[0])
            node2 = int(l[1])
            weight = int(l[2])
            
            v_set.add(node1)
            v_set.add(node2)
            
            edges_dict[(node1,node2)] = weight
            
    return v_set, edges_dict

def primMST(v_set, edges_dict):
    explored = set()
    tree_cost = 0
    explored.add(1)
    
    while explored != v_set:
        min_crossing_edge = []
        edges_to_delete = []
        for key in edges_dict: # each key is a tuple
            if (key[0] in explored and key[1] not in explored) or key[1] in explored and key[0] not in explored:
                if not min_crossing_edge or min_crossing_edge[1] > edges_dict[key]:
                    min_crossing_edge = [key, edges_dict[key]]
            if key[0] in explored and key[1] in explored:
                edges_to_delete.append(key)
                
        # delete edges where both vertices are already in the explored region        
        for i in edges_to_delete:
            del edges_dict[i]
            
        # minimum crossing edge was found from above for loop
        tree_cost += edges_dict[min_crossing_edge[0]]
        explored.add(min_crossing_edge[0][0])
        explored.add(min_crossing_edge[0][1])
        
    return tree_cost
    
def main(filename):
    v_set,edges_dict = read_from_file(filename)
    
    cost = primMST(v_set, edges_dict)
    print (cost)

main("edges.txt")
#main("test.txt")