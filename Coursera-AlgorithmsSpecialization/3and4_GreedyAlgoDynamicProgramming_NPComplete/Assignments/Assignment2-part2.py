# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 2, Part 2 of 2
# Python 2.7.10
#
# Part 2: Given a list of binary nodes with 1s and 0s, determine the largest
# value of k such that there is a k-clustering with spacing at least 3.
# i.e. no nodes in separate clusters with spacing 2 or less
# Spacing defined as Hamming distance: the number of differing bits between
# two nodes' labels. Note: duplicates exist.

import fileinput

def read_from_file(filename):
    """For Part 2: Reads a file containing binary nodes in Hamming distance
    and returns the set of all nodes."""

    node_to_leader_dict = {} # maps the node to the cluster number
    leader_to_nodes_dict = {} # maps the leader to a set of all nodes under leader

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) > 2:
            node = ()
            for i in l:
                node += (int(i),)

            if node not in node_to_leader_dict:
                node_to_leader_dict[node] = node

            if node not in leader_to_nodes_dict:
                leader_to_nodes_dict[node] = set()
                leader_to_nodes_dict[node].add(node) # leader contains its own node

    return node_to_leader_dict, leader_to_nodes_dict

def generate_closest(node):
    """Given a node as a tuple of size 24, returns the complete set of nodes
    with a Hamming distance from node of 0, 1, or 2, as a set of tuples"""
    closest = set()
    closest.add(node) # Node itself has a distance of 0

    # Generate closest nodes with distance of 1
    i = 0
    while i < len(node):
        if node[i] == 0:
            new_node = node[:i] + (1,) + node[i + 1:]
        else:
            new_node = node[:i] + (0,) + node[i + 1:]
        closest.add(new_node)
        i += 1

    # Generate closest nodes with distance of 2
    i = 0
    while i < len(node) - 1:
        if node[i] == 0:
            num1 = 1
        else:
            num1 = 0
        j = i + 1
        while j < len(node):
            if node[j] == 0:
                num2 = 1
            else:
                num2 = 0

            new_node = node[:i] + (num1,) + node[i + 1:j] + (num2,) + node[j + 1:]
            closest.add(new_node)
            j += 1
        i += 1

    return closest

def consolidate_leaders(node, leaders_to_consolidate, leader_to_nodes_dict,
node_to_leader_dict):
    # find leader with the most nodes and make that the main leader
    leaders_to_consolidate.add(node)
    size = 0
    largest_leader = node
    for l in leaders_to_consolidate:
        if len(leader_to_nodes_dict[l]) > size:
            size = len(leader_to_nodes_dict[l])
            largest_leader = l

    leaders_to_consolidate.remove(largest_leader)

    for l in leaders_to_consolidate:
        # take nodes under leader l and puts it under leader largest_leader
        leader_to_nodes_dict[largest_leader].update(leader_to_nodes_dict[l])
        # sets all nodes under l to point to largest leader
        for node in leader_to_nodes_dict[l]:
            node_to_leader_dict[node] = largest_leader
        # delete leader l
        del leader_to_nodes_dict[l]

def maxkclustering(node_to_leader_dict, leader_to_nodes_dict):
    """Returns maximum k clustering such that there is Hamming spacing of at
    least 3"""

    i = 0
    for node in node_to_leader_dict:
        closest_nodes = generate_closest(node)

        leaders_to_consolidate = set()
        for nearby_node in closest_nodes:
            # if this generated close node exists in file and is not in a
            # cluster of size > 1, set its leader to central node
            if nearby_node in node_to_leader_dict:
                nearby_node_leader = node_to_leader_dict[nearby_node]

                if len(leader_to_nodes_dict[nearby_node_leader]) <= 1:
                    # nearby node is in itself a single cluster so
                    # we make its leader the central node
                    leader_to_nodes_dict[node].add(nearby_node)
                    node_to_leader_dict[nearby_node] = node
                elif len(leader_to_nodes_dict[nearby_node_leader]) > 1:
                    # there's another cluster to which this node belongs
                    # so we need to keep track of this and consolidate
                    # the leaders later
                    leaders_to_consolidate.add(nearby_node_leader)

        consolidate_leaders(node, leaders_to_consolidate,
        leader_to_nodes_dict, node_to_leader_dict)

        if i % 100 == 0:
            print "On the ", i, "th node, number of leaders: ", len(leader_to_nodes_dict)
        i += 1

    return len(leader_to_nodes_dict)

def main(filename):
    node_to_leader_dict, leader_to_nodes_dict = read_from_file(filename)
    print maxkclustering(node_to_leader_dict, leader_to_nodes_dict)

    print "done"

main("clustering_big.txt")
#main("test.txt")
