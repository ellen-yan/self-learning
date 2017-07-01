# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 2, Part 1 of 2
# Python 2.7.10
#
# Part 1: Given a list of edges and the cost of the edges (to make a graph),
# run the clustering algorithm where the target number k of clusters is set
# to 4. What is the maximum spacing of a 4-clustering?

# note: remove smallest distances first

import fileinput

def read_from_file(filename):
    """For Part 1: Reads a file containing edges in the formate node1 node2
    weight and returns the graph in a dictionary mapping edges to weights.
    node1 is always less than node2, and distances are positive but not distinct."""

    edge_dict = {} # maps the weight of the edge to a list of the nodes, each pair is sequential
    node_to_leader_dict = {} # maps the node to the cluster number
    leader_to_nodes_dict = {} # maps the leader to a set of all nodes under leader

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) != 1:
            node1 = int(l[0])
            node2 = int(l[1])
            weight = int(l[2])
            # maps weight of the edge to list of nodes
            if weight not in edge_dict:
                edge_dict[weight] = [node1, node2]
            else:
                edge_dict[weight].append(node1)
                edge_dict[weight].append(node2)
            # the leader of the cluster is each individual point in the beginning
            if node1 not in node_to_leader_dict:
                node_to_leader_dict[node1] = node1
            if node2 not in node_to_leader_dict:
                node_to_leader_dict[node2] = node2
            if node1 not in leader_to_nodes_dict:
                leader_to_nodes_dict[node1] = set()
                leader_to_nodes_dict[node1].add(node1)
            if node2 not in leader_to_nodes_dict:
                leader_to_nodes_dict[node2] = set()
                leader_to_nodes_dict[node2].add(node2) # leader contains its own node

    return edge_dict, node_to_leader_dict, leader_to_nodes_dict

def kcluster(edge_dict, node_to_leader_dict, leader_to_nodes_dict, k):
    for weight in edge_dict: # loop through dict from low to high weight
        if len(leader_to_nodes_dict) <= k:
            print "broke out of loop with weight ", weight
            break
        # list of nodes with this edge weight
        node_list = edge_dict[weight]
        i = 0
        while i < len(node_list):
            if len(leader_to_nodes_dict) <= k:
                print "broke out of loop with weight", weight
                break

            # first node of a pair: handle both pairs
            leader1 = node_to_leader_dict[node_list[i]]
            leader2 = node_to_leader_dict[node_list[i + 1]]
            if leader1 == leader2:
                i += 2
                continue
            if len(leader_to_nodes_dict[leader1]) <= len(leader_to_nodes_dict[leader2]):
                smaller_leader = leader1
                larger_leader = leader2
            else:
                smaller_leader = leader2
                larger_leader = leader1

            # merge smaller_leader's nodes to larger_leader's
            # - transfer all nodes from smaller_leader to larger_leader
            # - change all nodes pointing to smaller_leader to point to larger_leader
            # - delete smaller_leader

            leader_to_nodes_dict[larger_leader] = (
            leader_to_nodes_dict[larger_leader] | leader_to_nodes_dict[smaller_leader])
            for e in leader_to_nodes_dict[smaller_leader]:
                node_to_leader_dict[e] = larger_leader

            del leader_to_nodes_dict[smaller_leader]

            i += 2

    # need to find the smallest weight that goes through nodes that have
    # different leaders

    for weight in edge_dict:
        i = 0
        node_list = edge_dict[weight]
        while i < len(node_list):
            node1 = node_list[i]
            node2 = node_list[i + 1]
            if node_to_leader_dict[node1] != node_to_leader_dict[node2]:
                return weight
            i += 2
    return

def main(filename):
    edge_dict, node_to_leader_dict, leader_to_nodes_dict = read_from_file(filename)
    k = 4
    print kcluster(edge_dict, node_to_leader_dict, leader_to_nodes_dict, k)


main("clustering1.txt")
#main("test.txt")
