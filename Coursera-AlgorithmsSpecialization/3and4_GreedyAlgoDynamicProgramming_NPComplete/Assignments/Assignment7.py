# Coursera, Stanford Algorithms Specialization
# Course 4, Dynamic Programming, All Pairs Shortest Paths, NP Complete
# Assignment 2
# Python 2.7.10
#
# Implements the nearest neighbor heuristic for the traveling salesman
# problem. Given a file that contains the x and y coordinates of a city's
# location, starts tour at the first city and repeatedly visits the closest
# city that the tour hasn't visited yet. In case of tie, go to closest city
# with the lowest index. Returns to the first city to complete the tour after
# visiting each city exactly once.

import fileinput
import math

def read_from_file(filename):
    """Reads in a file containing a list of x and y coordinates for cities.
    Returns a list of tuples where each tuple is the (x, y) coordinate"""
    coordinates = [] # list of city coordinates as a tuple
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) > 1:
            coordinates.append((float(l[1]), float(l[2])))
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
        if i % 1000 == 0:
            print "Finished initializing row %d" % i
    print "Finished initializing blank distances list"

    # updates 2D list of distances with appropriate values based on coordinates
    i = 0
    for coord in coordinates_list:
        cities_set.add(i + 1)
        j = i
        for coord2 in coordinates_list[i:]:
            distance = compute_euclidean_distance(coord, coord2)
            distances_list[i][j] = distance
            distances_list[j][i] = distance
            j += 1
        i += 1
        if i % 1000 == 0:
            print "Computed all coordinates up to %dth city" % i

    return cities_set, distances_list

def find_nearest(city_index, distances_2D_list, visited_cities):
    """Given the index of a city, 2D list of distances between cities, and a
    set of all visited cities, returns the city index that is nearest to
    this city that is not in the set of visited cities."""

    closest = None
    min_distance = float("inf")
    i = 0
    while i < len(distances_2D_list[city_index]):
        dist = distances_2D_list[city_index][i]
        if dist < min_distance and (i + 1) not in visited_cities:
            min_distance = dist
            closest = i
        i += 1
    return closest

def nearest_neighbor_tsp(cities_set, distances_2D_list):
    """Nearest neighbor heuristic applied to the traveling salesman problem.
    Starts tour at first city, then repeatedly visits the closest city that
    the tour hasn't visited yet. In case of tie, goes to closest city with
    lowest index. Once every city has been visited exactly once, returns to
    first city to complete the tour."""

    visited_set = set([1])
    current_city = 1
    traveled_distance = 0

    while visited_set != cities_set:
        next_city = find_nearest(current_city - 1, distances_2D_list, visited_set) + 1
        traveled_distance += distances_2D_list[current_city - 1][next_city - 1]
        visited_set.add(next_city)
        current_city = next_city
        if len(visited_set) % 100 == 0:
            print "Visited", len(visited_set), "cities"

    # need to travel back to 1 from the last city
    traveled_distance += distances_2D_list[0][current_city - 1]

    return traveled_distance

def main(filename):
    coordinates_list = read_from_file(filename)
    print "Finished reading file"
    cities_set, distances_2D_list = get_distances(coordinates_list)
    print "Finished initializing cities_set and distance list..."
    print nearest_neighbor_tsp(cities_set, distances_2D_list)
    print "done"


main("nn.txt")
#main("test.txt")
