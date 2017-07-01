# Coursera, Stanford Algorithms Specialization
# Course 2, Graph Search
# Assignment 2
#
# Computing shortest-path distances for directed graph using Dijkstra's algorithm
# Specifically, shortest-paths to vertices:
# 7,37,59,82,99,115,133,165,188,197

import fileinput

def read_from_file(filename):
    """Reads with multiple integers per line indicating
    vertices connected by directed edges and returns a list of vertices and
    edges for the directed graph"""
    
    edges_dict = {}
    vertices_set = set()
    
    for line in fileinput.input([filename]):
        l = line.split() # produces list of strings, each a string separated from each other with tabs in the file
        
        vertices_set.add(int(l[0]))
        edges_dict[int(l[0])] = []
        
        for e in l[1:]:
            vertex_length = e.split(",")
            # Edges are stored in dictionaries where tail vertex maps to a list of lists: [[head vertex, length],[head vertex, length]...]
            edges_dict[int(l[0])].append([int(vertex_length[0]),int(vertex_length[1])])
    
    return vertices_set, edges_dict

def shortestPaths(v_set,e_dict,source_v):
    """Computes shortest paths from source_v (int) to all other vertices in
    v_set using edges from e_dict. Returns a dictionary mapping vertices to
    their shortest path from source_v"""
    
    explored_vertices = set()
    explored_vertices.add(source_v)
    shortest_paths_dict = {}
    shortest_paths_dict[source_v] = 0
    
    while explored_vertices != v_set: # while not all vertices have been explored
        min_path_vertices = [] # List of vertices that result in the shortest path lengths on frontier: [source, dest]
        min_path_length = -1
        for key in e_dict: # loop through all edges in existence
            if key in explored_vertices: # if the source vertex is explored
                for dest_v in e_dict[key]: # loop through all possible destinations from this vertex
                    if dest_v[0] not in explored_vertices: # if destination vertex has not been explored...
                        if (dest_v[1] + shortest_paths_dict[key]) < min_path_length or min_path_length == -1: 
                            # if the length of vertices we're looking at is smaller than the minimum or if this is the first path we're looking at, set vertices with minimum path length to the total path length from the source vertex to end vertex
                            min_path_length = dest_v[1] + shortest_paths_dict[key]
                            min_path_vertices = [key, dest_v[0]]
                 
        explored_vertices.add(min_path_vertices[1])
        shortest_paths_dict[min_path_vertices[1]] = min_path_length
    
    return shortest_paths_dict #dict mapping vertices to their paths

def main(filename):
    v_set,e_dict = read_from_file(filename)
    print("File read")
  
    shortest_paths_dict = shortestPaths(v_set,e_dict, 1)
    print("Shortest paths:")
    print("Vertex 7:",shortest_paths_dict[7])
    print("Vertex 37:",shortest_paths_dict[37])
    print("Vertex 59:",shortest_paths_dict[59])
    print("Vertex 82:",shortest_paths_dict[82])
    print("Vertex 99:",shortest_paths_dict[99])
    print("Vertex 115:",shortest_paths_dict[115])
    print("Vertex 133:",shortest_paths_dict[133])
    print("Vertex 165:",shortest_paths_dict[165])
    print("Vertex 188:",shortest_paths_dict[188])
    print("Vertex 197:",shortest_paths_dict[197])

main("dijkstraData.txt")
#main("test.txt")