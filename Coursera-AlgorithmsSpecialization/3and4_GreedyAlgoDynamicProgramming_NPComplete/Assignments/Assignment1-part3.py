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
    
    key_heap = [] # contains a min-heap of keys for each vertex that keeps track of smallest weight connected to source node, infinity otherwise
    vkey_dict = {} # maps each node to the "key" of the node which is the smallest edge connecting node to source node (1)
    edges_dict = {} # maps the weight of the edge to tuples nodes with this edge weight (since weights may not be distinct)
    weight_dict = {} # maps a tuple of vertices to the edge weight
    v_set = set() # set of all vertices
    
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        
        if len(l) != 2:
            node1 = int(l[0])
            node2 = int(l[1])
            weight = int(l[2])
            new_key = float("inf")
            
            v_set.add(node1)
            v_set.add(node2)
            
            weight_dict[(node1,node2)] = weight
            
            if weight not in edges_dict:
                edges_dict[weight] = [(node1,node2)]
            else:
                edges_dict[weight].append((node1,node2))
            
            if node1 != 1:
                if node2 == 1:
                    vkey_dict[node1] = weight
                    new_key = weight
                else:
                    # Looking only at edges that don't include the source node
                    if node1 not in vkey_dict:
                        vkey_dict[node1] = float("inf")
                        new_key = float("inf")
                if new_key != float("inf"):
                    addToMinHeap(key_heap, new_key) #only add to heap if node1 is not source
            
            new_key = float("inf")
            if node2 != 1:
                if node1 == 1:
                    vkey_dict[node2] = weight
                    new_key = weight
                else:
                    if node2 not in vkey_dict:
                        vkey_dict[node2] = float("inf")
                        new_key = float("inf")
                
                if new_key != float("inf"):   
                    addToMinHeap(key_heap, new_key)
    
    return key_heap, edges_dict, vkey_dict, v_set, weight_dict

def addToMinHeap(heap, num):
    """A minimum heap maintained as a list, and an integer num to be added"""
    heap.append(num) # Adds number to last leaf
    
    if len(heap) <= 1: # If heap is only the root, return
        return
    
    num_index = len(heap) - 1
    parent_index = (int((num_index + 1) / 2) - 1)
    
    while heap[num_index] < heap[parent_index] and num_index != 0:
        
        # Swap positions of parent and child
        temp = heap[num_index]
        heap[num_index] = heap[parent_index]
        heap[parent_index] = temp
        
        num_index = parent_index
        parent_index = int((num_index + 1) / 2) - 1

def getRoot(heap):
    return heap[0]

def deleteMin(heap):
    # Deletes root from a minimum heap
    
    # Swap root and last element
    temp = heap[0]
    heap[0] = heap[-1]
    heap[-1] = temp
    
    root = heap.pop()
    
    if len(heap) <= 1:
        return root
    
    num_index = 0
    
    if len(heap) < 3:
        # swap child and parent and return
        temp = heap[0]
        heap[0] = heap[1]
        heap[1] = temp
        return root
    
    child_index1 = 1
    child_index2 = 2

    while (heap[num_index] > heap[child_index1] or heap[num_index] > heap[child_index2]):
        if child_index2 >= len(heap):
            child_index = child_index1
        else:
            if heap[child_index1] < heap[child_index2]:
                child_index = child_index1
            elif heap[child_index2] < heap[child_index1]:
                child_index = child_index2
        
        temp = heap[num_index]
        heap[num_index] = heap[child_index]
        heap[child_index] = temp
        
        num_index = child_index
        child_index1 = (num_index + 1) * 2 - 1
        child_index2 = (num_index + 1) * 2
        
        if child_index1 >= len(heap):
            return root
        elif child_index2 >= len(heap):
            # first child exists but second does not; only need to check the case when this child is not smaller than parent
            if heap[num_index] <= heap[child_index1]:
                return root        

    return root

def primMST(key_heap, edges_dict, vkey_dict, v_set, weight_dict):
    """Takes as arguments: a heap containing the keys to vertices on the frontier
    (where each key is the cheapest edge from inside the explored region to the unexplored),
    a dictionary of edges mapping the weight of edges to tuples of vertices with that edge weight,
    and a dictionary of vertices mapping the vertex to their key. The input assumes we start with
    vertex 1 as the source (explored) vertex."""
    
    explored = set() # set of vertices that have been explored
    tree_cost = 0 # will store the total cost of the minimum spanning tree which may or may not be negative
    
    explored.add(1) #set source vertex to 1
    
    while explored != v_set:
        cheapest_e = deleteMin(key_heap) # may not exist, need to check that vertices are in correct sets
        added = False
        if cheapest_e in edges_dict:
            possible_nodes = edges_dict[cheapest_e]
            for e in possible_nodes: # each element e is a tuple (x,y) of vertices x, y
                if e[0] in explored and e[1] not in explored:
                    tree_cost += cheapest_e
                    explored.add(e[1])
                    new_vertex = e[1]
                    added = True
                elif e[1] in explored and e[0] not in explored:
                    tree_cost += cheapest_e
                    explored.add(e[0])
                    new_vertex = e[0]
                    added = True

                if added:
                    # add to heap the keys which are based on the vertex that was just added
                    for value in list(edges_dict.values()):
                        for e in value: # e is a tuple
                            if e[0] == new_vertex and e[1] not in explored:
                                # add to heap the key of the other vertex in tuple and update the edges_dict, and update vkey_dict (use
                                # vkey_dict to change edges_dict by calling vkey_dict to find the old key of the vertex)
                                v = e[0]
                                w = e[1]
                                old_key_w = vkey_dict[w]
                                
                                if (v, w) in weight_dict:
                                    new_key_w = weight_dict[(v,w)]
                                    if new_key_w < old_key_w:
                                        vkey_dict[w] = new_key_w
                                        addToMinHeap(key_heap, new_key_w)
                                elif (w,v) in weight_dict:
                                    new_key_w = weight_dict[(w,v)]
                                    if new_key_w < old_key_w:
                                        vkey_dict[w] = new_key_w
                                        addToMinHeap(key_heap, new_key_w)
                                
                            if e[1] == new_vertex and e[0] not in explored:
                                v = e[1]
                                w = e[0]
                                old_key_w = vkey_dict[w]
                                if (v, w) in weight_dict:
                                    new_key_w = weight_dict[(v,w)]
                                    if new_key_w < old_key_w:
                                        vkey_dict[w] = new_key_w
                                        addToMinHeap(key_heap, new_key_w)
                                elif (w,v) in weight_dict:
                                    new_key_w = weight_dict[(w,v)]
                                    if new_key_w < old_key_w:
                                        vkey_dict[w] = new_key_w
                                        addToMinHeap(key_heap, new_key_w)
                    break
                
def main(filename):
    key_heap, edges_dict, vkey_dict, v_set, weight_dict = read_from_file(filename)
    print(edges_dict)
    print(vkey_dict)
    print(key_heap)
    primMST(key_heap, edges_dict, vkey_dict, v_set, weight_dict)
    print ("done")
    

main("test.txt")
