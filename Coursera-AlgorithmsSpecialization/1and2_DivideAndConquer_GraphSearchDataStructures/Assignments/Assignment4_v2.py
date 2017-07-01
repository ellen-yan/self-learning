# Coursera, Stanford Algorithms Specialization
# Course 1, Divide and Conquer
# Assignment 4 version 2
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
    returns a list of edges containing the vertices associated with the edge"""
    
    whole_file = file.readlines() # list of strings each containing a line
    edges = []
    vertices = []
    
    for line in whole_file:
        l = line.split() # produces list of strings, each a number (e.g. '3') separated from each other with tabs in the file
        vertices.append(l[0])
        i = 1
        while i < len(l):
            if l[i] > l[0]:
                edges.append([l[0], l[i]])
            i += 1
    
    return vertices, edges

def collapseRandomVertices(v_list,e_list):
    random_index = random.randint(0,len(e_list) - 1) # for picking the edge to remove
    #random_index = 0
    source_vertex = e_list[random_index][0] # vertex that will be collapsed
    dest_vertex = e_list[random_index][1] # vertex into which source_vertex is collapsing into
    
    #print ("remove: ", source_vertex)
    #print("collapse into: ",dest_vertex)
    
    # all edges pointing to source_vertex will be modified to point to dest_vertex
    
    # Change all references to source vertex to destination vertex
    # Remove elements of edge list where both vertices
    
    for e in e_list:
        if e[0] == source_vertex:
            e[0] = dest_vertex
        if e[1] == source_vertex:
            e[1] = dest_vertex
    
    keep_going = True   
    i = 0
    while i < len(e_list):
        while keep_going and i < len(e_list):
            if e_list[i][0] == e_list[i][1]:
                e_list.remove(e_list[i])
                keep_going = True
            else:
                keep_going = False
        keep_going = True
        i += 1
    
    # Remove the source vertex from vertices list
    for v in v_list:
        if v == source_vertex:
            v_list.remove(v)
            break
            
def minCut(v_list, e_list):
    # Collapse the graph while there remains more than two vertices
    while len(v_list) > 2:
        collapseRandomVertices(v_list, e_list)
    
    return int(len(e_list))


def main(filename):
    i = 0
    minimum_found = 100
    while i < 300000:
        file_object = open_file_to_read(filename)
        v_list,e_list = read_from_file(file_object)
        close_file(file_object)
        
        trial = minCut(v_list,e_list)
        #print(v_list,e_list)
        if trial < minimum_found:
            minimum_found = trial
        print (trial)
        if i % 500 == 0:
            print ("min so far: ", minimum_found, ", current trial is ", i)
        i += 1
        
    print ("final min: ", minimum_found)


main("kargerMinCut.txt")
#main("test.txt")

#print(set([1,2,3]) == set([1,3,2])) # True
#print([1,2,3] == [2,3,1]) # False
