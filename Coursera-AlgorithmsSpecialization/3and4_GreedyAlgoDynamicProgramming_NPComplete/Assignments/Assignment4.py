# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms, Dynamic Programming
# Assignment 4, Parts 1 and 2 of 2
# Python 2.7.10
#
# Computes the value of the optimal solution to the knapsack problem given
# a file containing the value and weight of each object on separate lines,
# with the i-th line denoting the i-th object. Can assume all numbers are
# positive and item weights and knapsack capacity are integers.

import fileinput

def read_from_file(filename):
    """Reads in a file containing a list of values and weights for objects
    to be considered in the knapsack problem. On the i-th line is given the
    value and weight of the object for the i-ith item. Can assume all numbers
    are positive and item weights and knapsack capacity are integers. First
    line contains the knapsack size."""

    value_list = [] # list of values of the i-th object in position i - 1
    weight_list = [] # list of weights of the i-th object in position i - 1
    knapsack_capacity = 0

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) == 1:
            knapsack_capacity = int(l[0])
            continue
        value_list.append(int(l[0]))
        weight_list.append(int(l[1]))

    return value_list, weight_list, knapsack_capacity

def knapsack_optimal_value(value_list, weight_list, knapsack_capacity):
    best_values_2D_list = []

    # initialize 2D list
    for i in range(0, len(value_list) + 1):
        best_values_2D_list.append([])

    # with no items in knapsack, values for any knapsack capacity are zero
    for w in range(0, knapsack_capacity + 1):
        best_values_2D_list[0].append(0)

    # looping over i, the number of items in the array
    for i in range(1, len(value_list) + 1):

        for w in range(0, knapsack_capacity + 1):

            if weight_list[i - 1] > w:
                new_value = best_values_2D_list[i - 1][w]
            else:
                new_value = max(best_values_2D_list[i - 1][w],
                                best_values_2D_list[i - 1][w - weight_list[i - 1]]
                                + value_list[i - 1])

            best_values_2D_list[i].append(new_value)

        print "finished column %d out of %d" % (i, len(value_list))

    return best_values_2D_list[-1][-1]

def main(filename):
    value_list, weight_list, knapsack_capacity = read_from_file(filename)
    best_value = knapsack_optimal_value(value_list, weight_list, knapsack_capacity)
    print best_value
    print "done"

#main("knapsack1.txt")
main("knapsack_big.txt")
#main("test.txt")
