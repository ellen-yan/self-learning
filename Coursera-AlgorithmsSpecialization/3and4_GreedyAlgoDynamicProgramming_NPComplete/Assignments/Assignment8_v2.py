# Coursera, Stanford Algorithms Specialization
# Course 4, Dynamic Programming, All Pairs Shortest Paths, NP Complete
# Assignment 2, version 2
# Python 2.7.10
#
# Solves the 2-SAT problem on six files using strongly connected components
# and determines which given files are solvable. In the input, a '-' indicates
# logical not, and the numbers indicate the variable number. For example,
# given "-23 4", means "not x23 or x4". Can assume that each pair of variables
# used in a clause appears as a pair at most once and variables cannot be a 0.
# Note that the variable numbers are not restricted to be below the number of
# clauses.
# **Much more efficient than Papadimitriou's algorithm, operates in linear time

import fileinput

def read_from_file(filename):
    """Reads in a file containing a list of clauses for variables, where '-'
    denotes logical not, and variables are given as the variable number.
    Returns a list of clauses, where each clause is represented as a tuple,
    and a set of all variable names. Converts this into a graph and returns
    a set of vertices and edges for the directed graph. For each clause,
    (u OR v), adds edges ~u -> v and ~v -> u to graph."""

    edges = {}
    reverse_edges = {}
    vertices = set()

    for line in fileinput.input([filename]):
        l = line.split() # produces list of strings, each a number (e.g. '3') separated from each other with tabs in the file

        if len(l) > 1:
            v1 = int(l[0])
            v2 = int(l[1])
            # add ~u -> v edge
            if v1 * -1 not in edges:
                edges[v1 * -1] = [v2]
            else:
                edges[v1 * -1].append(v2)
            # add ~v -> u edge
            if v2 * -1 not in edges:
                edges[v2 * -1] = [v1]
            else:
                edges[v2 * -1].append(v1)

            # add edges above to reverse_edges
            if v2 not in reverse_edges:
                reverse_edges[v2] = [v1 * -1]
            else:
                reverse_edges[v2].append(v1 * -1)
            if v1 not in reverse_edges:
                reverse_edges[v1] = [v2 * -1]
            else:
                reverse_edges[v1].append(v2 * -1)

            vertices.add(v1)
            vertices.add(v1 * -1)
            vertices.add(v2)
            vertices.add(v2 * -1)

    return vertices, edges, reverse_edges

def depthFirstSearchMain(v_set,e_dic,reverse_e_dic):

    explored = set()
    time = 0
    finish_time_dic = {}
    time_to_vertex_dic = {}
    for i in v_set:
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
                    time_to_vertex_dic[time] = v

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
                leader[s] = []
                stack = [s]
                while stack:
                    v = stack.pop()
                    if v not in explored:
                        explored.add(v)
                        leader[s].append(v)
                        if v in new_e_dic:
                            for w in new_e_dic[v]:
                                if w not in explored: stack.append(w)

    # See if there are any leaders that contain both a variable and iterations
    # complement

    for l in leader.values():
        converted_back = set()
        for t in l:
            converted_back.add(time_to_vertex_dic[t])
        for i in converted_back:
            if i * -1 in converted_back:
                return False
    return True

def main(filename):
    v_set,e_dic,reverse_e_dic = read_from_file(filename)
    print("File read")

    satisfied = depthFirstSearchMain(v_set,e_dic,reverse_e_dic)
    print "Valid assignment found for file %s?: %s" % (filename, satisfied)



main("2sat1.txt")
main("2sat2.txt")
main("2sat3.txt")
main("2sat4.txt")
main("2sat5.txt")
main("2sat6.txt")
#main("test.txt")
