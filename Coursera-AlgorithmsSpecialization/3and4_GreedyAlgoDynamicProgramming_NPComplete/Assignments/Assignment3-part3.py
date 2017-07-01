# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms, Dynamic Programming
# Assignment 3, Part 3 of 3
# Python 2.7.10
#
# Part 3: Computes maximum-weight independent set of a path graph given a
# list of the weights for each vertex (one entry per line) with the vertex
# number given by the order in which it appears in the file.
# Question: determine which of the vertices 1, 2, 3, 4, 17, 117, 517, and 997
# belong to the maximum-weight independent set.

import fileinput

def read_from_file(filename):
    """For Part 3: Reads in a file containing a list of weights of each
    vertex as part of a path graph, with the vertex number indicated by the
    order in which it appears. Returns a list of weights with vertex i in
    list position (index) i - 1."""

    weight_list = [] # list of weights, vertex i in position i - 1

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        weight_list.append(int(l[0]))

    return weight_list

def get_maxweight_list(weight_list):
    """Given a list of weights with index i representing vertex i + 1,
    returns a list corresponding to the maximum-weight of the maximum-weight
    independent set up to and including the vertex at position i, stored at
    position i in the returned list."""

    mw_list = []
    # maximum-weight independent set of one vertex is its own weight
    mw_list.append(weight_list[0])
    # maximum-weight independent set of two connected vertices is the higher one
    mw_list.append(max(weight_list[0], weight_list[1]))

    # for all the rest of the vertices, find maximum-weight of the MWIS at each
    # position corresponding to the given weight_list
    i = 2
    while i < len(weight_list):
        mw_list.append(max(mw_list[i - 1],
        mw_list[i - 2] + weight_list[i]))
        i += 1

    return mw_list

def get_mwis(mw_list, weight_list):
    """Given a list of the maximum-weight independent set up to and including
    the position i in mw_list, and the weight of each vertex stored in
    weight_list, returns a set of all vertices which are part of the
    maximum-weight independent set of this list. Any vertex i is at position
    i - 1 in both lists."""

    mwis_set = set()

    i = len(mw_list) - 1
    while i > 1:
        # special case where i == 2 or i == 3, we want to handle it here
        if i == 2 and mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            # element at index 2 is not in MWIS, just add the maximum-weight
            # vertex from 0th and 1st position

            vertex = -1
            if mw_list[0] >= mw_list[1]:
                vertex = 1
            else:
                vertex = 2

            mwis_set.add(vertex)

        elif i == 2 and mw_list[i - 1] < (mw_list[i - 2] + weight_list[i]):
            # element at index 2 is in MWIS, just add this element and
            # the element at the 0th position
            mwis_set.add(3) # correct
            mwis_set.add(1)
        elif i == 3 and mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            # element at index 3 is not in MWIS, just increment down 1
            i -= 1
        elif i == 3 and mw_list[i - 1] < (mw_list[i - 2] + weight_list[i]):
            # element at index 3 is in MWIS, then we need to check if element
            # at index 2 is in the MWIS. If 2 is not, then add the maximum
            # between index 0 and 1; otherwise, if 2 is, then add index 2
            # and index 0
            if mw_list[1] >= (mw_list[0] + weight_list[2]):
                # element at index 2 not in MWIS
                vertex = -1
                if mw_list[0] >= mw_list[1]:
                    vertex = 1
                else:
                    vertex = 2

                mwis_set.add(vertex)

            elif mw_list[1] < (mw_list[0] + weight_list[2]):
                # element at index 2 is in MWIS, add this and index 0 vertex
                mwis_set.add(3) # correct
                mwis_set.add(1)


        if mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            i -= 1 # i-th element not in mw_set, just increment down one
        else:
            mwis_set.add(i + 1)
            # i-th element is in mw_set, add it and skip the next vertex
            i -= 2
    return mwis_set

def main(filename):
    weight_list = read_from_file(filename)
    mw_list = get_maxweight_list(weight_list)
    mw_set = get_mwis(mw_list, weight_list)
    print "Set of indices: ", mw_set

main("mwis.txt")
#main("test.txt")
