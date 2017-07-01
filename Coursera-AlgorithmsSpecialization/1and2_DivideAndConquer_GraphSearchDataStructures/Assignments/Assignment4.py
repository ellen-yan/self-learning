# Coursera, Stanford Algorithms Specialization
# Course 1, Divide and Conquer
# Assignment 4
#
# Computing minimum number of cuts in a graph from file

import random

def open_file_to_read(filename):
    int_file = open(filename,"r")
    return int_file

def close_file(file):
    file.close()

def read_from_file(file):
    """Takes a parameter file object with multiple integers per line and
    returns a list of vertices referring to edges, and a list of edges containing
    the vertices associated with the edge at each index in the list"""
    
    whole_file = file.readlines() # list of strings each containing a line
    vertices = []
    edges = []
    
    vertex_index = -1
    key = 0
    for line in whole_file:
        vertex_index += 1
        l = line.split() # produces list of strings, each a number (e.g. '3') separated from each other with tabs in the file
        vertices.append([l[0], []])
        
        i = 1
        while i < len(l):
            edges.append([key,[l[0], l[i]]])
            
            vertices[len(vertices) - 1][1].append(edges[-1][0]) #key of last edge added
            # is appended to the second element of the last element in vertices
            i += 1
            key += 1
    
    #Note: the index of the last position in edges list is one less than the number of edges
    return vertices, edges

def collapseRandomVertices(v_list, e_list):
    random_index = random.randint(0,len(e_list) - 1) # for picking the edge to remove
    #random_index = 0
    source_vertex = e_list[random_index][1][0] # vertex that will be collapsed
    dest_vertex = e_list[random_index][1][1] # vertex into which source_vertex is collapsing into
    
    # all edges pointing to source_vertex will be modified to point to dest_vertex
    
    #1: need to get all the edges that are connected to source_vertex
    #list_source_edges = [] # For storing a list of integers referencing the edges that contain the source vertex
    #i = 0
    #while len(list_source_edges) == 0:
        
    #    if v_list[i][0] == source_vertex:
    #        list_source_edges = v_list[i][1]
    #    i += 1
    
    #2.1: look at all the edges connected to source_vertex, and change the source_vertex
    # value in the list to that of dest_vertex
    
    for e in e_list:
        if e[1][0] == source_vertex:
            e[1][0] = dest_vertex
        elif e[1][1] == source_vertex:
            e[1][1] = dest_vertex
    
    #3: remove the source_vertex from the list of vertices
    for v in v_list:
        if v[0] == source_vertex:
            v_list.remove(v)
            break
    
    #4: go through edges list and remove all lists that contain two of the same elements (i.e. self loops)
    for e in e_list:
        if e[1][0] == e[1][1]:
            e_list.remove(e)
            
    #5: reconstruct v_list from e_list using existing vertices
    new_v_list = []
    for vertex in v_list:
        new_v_list.append([vertex[0],[]])
        for e in e_list:
            if e[1][0] == vertex[0] or e[1][1] == vertex[0]:
                new_v_list[-1][1].append(e[0])
    v_list = new_v_list
            
def minCut(v_list, e_list):
    while len(v_list) > 2:
        collapseRandomVertices(v_list, e_list)
    for e in e_list:
        if e[1][0] == e[1][1]:
            e_list.remove(e)
    
    return int(len(e_list)/2)


def main(filename):
    trial_results = []
    i = 0
    while i < 40000:
        file_object = open_file_to_read(filename)
        v_list, e_list = read_from_file(file_object)
        close_file(file_object)       
        
        trial = minCut(v_list,e_list)
        trial_results.append(trial)
        print (trial)
        if i % 100 == 0:
            print ("min so far: ", min(trial_results))
        i += 1
        
    print ("final min: ", min(trial_results))


main("kargerMinCut.txt")

#print(set([1,2,3]) == set([1,3,2])) # True
#print([1,2,3] == [2,3,1]) # False
