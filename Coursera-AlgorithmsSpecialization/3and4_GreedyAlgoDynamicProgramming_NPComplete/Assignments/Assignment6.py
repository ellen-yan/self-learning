# Coursera, Stanford Algorithms Specialization
# Course 4, Dynamic Programming, All Pairs Shortest Paths, NP Complete
# Assignment 2
# Python 2.7.10
#
# Implements a dynamic programming algorithm for the traveling salesman
# problem. Given a file that contains the x and y coordinates of a city's
# location, determines the minimum cost of a traveling salesman tour,
# where the distances between two cities is defined as the Euclidean distance.
# All cities have paths/edges to all other cities, and x and y coordinates
# are decimal numbers.

import fileinput
import math
import copy

def read_from_file(filename):
    """Reads in a file containing a list of x and y coordinates for cities.
    Returns a list of tuples where each tuple is the (x, y) coordinate"""

    coordinates = [] # list of city coordinates as a tuple

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) > 1:
            coordinates.append((float(l[0]), float(l[1])))

    return coordinates

def compute_euclidean_distance(tup1, tup2):
    """Given two tuples (x1, y1) and (x2, y2), returns the Euclidean distance
    between these tuples."""
    return math.sqrt((tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2)

def get_distances(coordinates_list):
    """Given a list of tuples each representing a city's x and y coordinates,
    returns the set of all cities (numbered 1 to n), and a 2D list of distances
    where position i, j (or j, i) in the 2D list is the Euclidean distance
    between cities i - 1 and j - 1"""

    cities_set = set()
    distances_list = []

    # initializes 2D list with 0's filled in
    for i in range(0, len(coordinates_list)):
        distances_list.append([])
        for j in range(0, len(coordinates_list)):
            distances_list[i].append(0)

    i = 0
    for coord in coordinates_list:
        cities_set.add(i + 1)
        j = 0
        for coord2 in coordinates_list:
            distance = compute_euclidean_distance(coord, coord2)
            distances_list[i][j] = distance
            distances_list[j][i] = distance
            j += 1
        i += 1

    return cities_set, distances_list

def get_subsets(input_set, subset_size, mandatory_elements):
    """Given a set of values and a subset size and a set of mandatory elements
    desired in the new subsets, returns a list of all possible combinations of
    subsets with the given subset size (assuming elements in
    set are integers). Algorithm uses brute-force and recursion"""

    list_of_sets = [] # list of all sets with size subset_size and less

    new_set = mandatory_elements.copy()
    if len(new_set) >= subset_size:
        list_of_sets.append(new_set)
        return list_of_sets

    all_values = list(input_set)

    # recursively get list of all sets with one smaller size
    subset_list = get_subsets(input_set, subset_size - 1, mandatory_elements)
    list_of_sets = copy.copy(subset_list)
    print "Obtained the subsets up to", subset_size - 1, "with length", len(subset_list)

    # recrusive call above, below: add single element to each subset in subset_list
    # if element in subset_list has size subset_size - 1
    for s in reversed(subset_list):
        if len(s) == subset_size - 1:
            new_set = s.copy()
            valid_values = set(all_values)
            valid_values.difference(s)
            # loops until a new element that doesn't exist in new_set has been added
            # to new_set and adds this to the list of new sets (without repeats)
            for i in valid_values:
                old_length = len(new_set)
                new_set.add(i)
                if len(new_set) == subset_size and new_set not in list_of_sets:
                    # append a copy of the set because sets are mutable
                    list_of_sets.append(new_set.copy())
                    if len(list_of_sets) % 10000 == 0:
                        print "length of list of sets is now", len(list_of_sets)
                    new_set.remove(i)
        else:
            break

    return list_of_sets

def traveling_salesman_min_cost(cities_set, distances_2D_list):
    """Given a set of all cities and a 2D list with position i, j (or j, i)
    denoting the distance between cities i - 1 and j - 1, returns the minimum
    cost of making a tour through all cities only once, assuming all cities
    are connected to all other cities."""

    # list of all sets starting from smaller size to larger
    master_set_list = []
    # total number of cities
    n = len(cities_set)

    master_set_list = get_subsets(cities_set, n, set([1]))

    print "Finished initializing subset list and dictionary"

    # 2D list to store information where set at position i, j gives minimum
    # cost of going to j + 1 visiting cities in set at position i, which
    # can be found in the master_set_list
    subset_destination_2D_list = []

    # initialize 2D list and fill in values for base case
    for i in range(0, len(master_set_list)):
        subset_destination_2D_list.append([])
        for j in range(0, n):
            if master_set_list[i] == set([1]):
                subset_destination_2D_list[i].append(0)
            else:
                subset_destination_2D_list[i].append(float("inf"))

    print "Finished base cases"

    # keep track of where we are in the master list
    i = 1
    # m is subproblem size
    for m in range(2, n + 1):
        # set up loop to only loop through sets of a certain size m
        while i < len(master_set_list) and len(master_set_list[i]) == m:
            # loop over all values in the set at position i
            for j in master_set_list[i]:
                if j != 1:
                    # finding copy of set minus j (i.e. internal cities)
                    # in master_set_list to refer to later
                    sub_s = master_set_list[i].copy()
                    sub_s.remove(j)
                    sub_s_position = master_set_list.index(sub_s)

                    minimum = float("inf")
                    for k in master_set_list[i]:
                        if k != j:
                            dist = (subset_destination_2D_list[sub_s_position][k - 1] +
                                distances_2D_list[k - 1][j - 1])
                            if dist < minimum:
                                minimum = dist
                    subset_destination_2D_list[i][j - 1] = minimum
            i += 1
        print "finished with subsets of size", m

    # find minimum from subset_destination_2D_list from all possible last destinations
    minimum = float("inf")
    for j in range(2, n + 1):
        cost = subset_destination_2D_list[-1][j - 1] + distances_2D_list[0][j - 1]
        if cost < minimum:
            minimum = cost
            print "minimum became the cost of going from vertex", j, "to 1"

    return minimum

def main(filename):
    coordinates_list = read_from_file(filename)
    cities_set, distances_2D_list = get_distances(coordinates_list)
    print "finished reading file and getting distances..."
    print traveling_salesman_min_cost(cities_set, distances_2D_list)
    print "done"

# Note: tsp.txt is too big. Looked at the plot visually, and split groups into
# two groups and tried overlapping combinations of the middle points to see
# how the main tour would be connected based on the existing connections at
# the edges of the groups in the smaller tours. Then combined the calculated
# values and subtracted any overlapping edges from adding smaller tours
#main("tsp1to13.txt")
#main("tsp.txt")
#main("test2.txt")

#test_set = set([1, 2, 3, 4, 5])
#print get_subsets(test_set, 3, set([1]))

# Sets cannot be used as keys in a dictionary or anywhere (not hashable)
