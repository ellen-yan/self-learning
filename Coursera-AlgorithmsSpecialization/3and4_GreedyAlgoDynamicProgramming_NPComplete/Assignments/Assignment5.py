# Coursera, Stanford Algorithms Specialization
# Course 4, Dynamic Programming, All Pairs Shortest Paths, NP Complete
# Assignment 1
# Python 2.7.10
#
# Computes the shortest path between any pair of vertices in a given directed
# graph (with possibly negative cycles). If there is a negative cycle, outputs
# that there is a negative cycle instead of the shortest path. Can assume
# all vertices appear at least once between the minimum and maximum values.
# Question requires running this algorithm on three different files.

import fileinput

def read_from_file(filename):
    """Reads in a file containing a list of vertices given as source vertex,
    destination vertex, and edge length per line. Returns a list of vertices
    in sorted order and a dictionary mapping vertices as tuples (source, dest)
    to the edge length."""

    v_set = set()
    v_list = [] # list of vertices in sorted order
    edge_dict = {} # dictionary mapping tuple (v1, v2) to edge length

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) > 2:
            v1 = int(l[0])
            v2 = int(l[1])
            v_set.add(v1)
            v_set.add(v2)
            edge_dict[(v1, v2)] = int(l[2])

    # convert set to sorted list
    v_list = sorted(list(v_set))

    return v_list, edge_dict

def apsp(v_list, edge_dict):
    """Uses the Floyd-Marshall algorithm to find the all-pairs shortest path
    on a graph which may or may not contain negative cycles. Returns None if
    there is a negative cycle, otherwise returns the shortest path found
    between any pair of vertices."""

    # 3D list where position i, j, k indicates vertex i + 1 going to
    # vertex j + 1, with vertices 1 to k inclusive indicating the set
    # of vertices which are allowed on the internal path from i + 1 to j + 1
    apsp_list = []
    n = len(v_list) # number of vertices

    # initialize base case
    for i in range(0, n):
        apsp_list.append([])
        for j in range(0, n):
            apsp_list[i].append([])
            if i == j:
                apsp_list[i][j].append(0)
            elif (i + 1, j + 1) in edge_dict:
                apsp_list[i][j].append(edge_dict[(i + 1, j + 1)])
            else:
                apsp_list[i][j].append(float("inf"))

    print "Finished initializing list"

    # append values to the end of third dimension (k) as calculated
    for k in range(1, n + 1): # k represents vertices 1 to k inclusive
        for i in range(0, n): # i is index of source vertex i + 1
            for j in range(0, n):

                apsp_list[i][j].append(min(apsp_list[i][j][k - 1],
                                      (apsp_list[i][k - 1][k - 1] +
                                      apsp_list[k - 1][j][k - 1])))

        if k % 100 == 0:
            print "Finished case for k =", k

    # check for negative cycles
    negative_cycle = False
    for i in range(0, n):
        if apsp_list[i][i][n] < 0:
            negative_cycle = True

    if negative_cycle:
        return None

    print "Checking shortest path..."
    shortest_path = apsp_list[0][0][n]
    for i in range(0, n):
        for j in range(0, n):
            if apsp_list[i][j][n] < shortest_path:
                shortest_path = apsp_list[i][j][n]

    return shortest_path

def main(filename):
    v_list, edge_dict = read_from_file(filename)
    #print v_list
    #print edge_dict
    s = apsp(v_list, edge_dict)
    print filename, "has shortest path ", s
    print "Finished for file ", filename

#main("g1.txt")
#main("g2.txt")
#main("g3.txt")
main("large.txt")
#main("test.txt")
