# Coursera, Stanford Algorithms Specialization
# Course 2, Graph Search
# Assignment 1, version 2
#
# Computing the 5 largest SCCs in a graph from file using iteration
# instead of recursion due to Python limitations, and with
# better data structures

import fileinput

def read_from_file(filename):
    """Reads a file with multiple integers per line indicating
    vertices connected by directed edges and returns a list of vertices and
    edges for the directed graph"""

    edges = {}
    reverse_edges = {}
    vertices = set()

    for line in fileinput.input([filename]):
        l = line.split() # produces list of strings, each a number (e.g. '3') separated from each other with tabs in the file

        # Adds edge to a dictionary with keys = tails and values = list of heads
        if int(l[0]) not in edges:
            edges[int(l[0])] = [int(l[1])]
        else:
            edges[int(l[0])].append(int(l[1]))

        if int(l[1]) not in reverse_edges:
            reverse_edges[int(l[1])] = [int(l[0])]
        else:
            reverse_edges[int(l[1])].append(int(l[0]))

        # Add vertices to list of vertices if not already in the list
        if int(l[0]) not in vertices:
            vertices.add(int(l[0]))
        if int(l[1]) not in vertices:
            vertices.add(int(l[1]))

        if len(vertices) % 100000 == 0:
            print ("Vertices read: ", len(vertices))

    return vertices, edges, reverse_edges

def depthFirstSearchMain(v_set,e_dic,reverse_e_dic):
    # define finishing time list, reverse graph, call the search twice here

    explored = set()
    time = 0
    finish_time_dic = {}
    for i in range(len(v_set),-1,-1):
        if i in v_set:
            stack = [i]
            while stack:
                v = stack.pop()
                if v not in explored:
                    explored.add(v)
                    stack.append(v)
                    if v in reverse_e_dic:
                        for w in reverse_e_dic[v]:
                            if w not in explored: stack.append(w)

                else:
                    if v not in finish_time_dic:
                        time += 1
                        finish_time_dic[v] = time

    # Resets explored dictionary and changes values of vertices to finishing
    # times for second pass
    leader = {}

    # Reset edges to point at the correct vertices since vertex values changed
    # to finishing time
    new_e_dic = {}
    new_v_set = set()
    for key in e_dic:
        new_key = finish_time_dic[key]
        new_e_dic[new_key] = []
        if new_key not in new_v_set:
            new_v_set.add(new_key)
        for value in list(e_dic[key]):
            new_value = finish_time_dic[value]
            new_e_dic[new_key].append(new_value)
            if new_value not in new_v_set:
                new_v_set.add(new_value)

    print("Starting second pass")

    explored = set()
    for i in range(len(new_v_set),-1,-1):
        if i in new_v_set:
            if i not in explored:
                s = i
                leader[s] = 0
                stack = [s]
                while stack:
                    v = stack.pop()
                    if v not in explored:
                        explored.add(v)
                        leader[s] += 1
                        if v in new_e_dic:
                            for w in new_e_dic[v]:
                                if w not in explored: stack.append(w)

    #Find the 5 largest SCCs using frequency of nodes being the leader,
    #and print out their sizes

    values = list(leader.values())
    for i in range(5):
        highest = max(values)
        print((i+1), "th highest: ",highest)
        values.remove(highest)

def main(filename):
    v_set,e_dic,reverse_e_dic = read_from_file(filename)
    print("File read")

    depthFirstSearchMain(v_set,e_dic,reverse_e_dic)



main("SCC.txt")
#main("scc_test4.txt")
#main("test.txt")
#main("test2.txt")
