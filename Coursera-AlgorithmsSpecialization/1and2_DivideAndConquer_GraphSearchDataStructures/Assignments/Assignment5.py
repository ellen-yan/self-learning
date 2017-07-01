# Coursera, Stanford Algorithms Specialization
# Course 2, Graph Search
# Assignment 1
#
# Computing minimum number of cuts in a graph from file using recursion

def open_file_to_read(filename):
    int_file = open(filename,"r")
    return int_file

def close_file(file):
    file.close()

def read_from_file(file):
    """Takes a parameter file object with multiple integers per line indicating
    vertices connected by directed edges and returns a list of vertices and
    edges for the directed graph"""
    
    whole_file = file.readlines() # list of strings each containing a line
    edges = []
    vertices = []
    explored = {}
    
    for line in whole_file:
        l = line.split() # produces list of strings, each a number (e.g. '3') separated from each other with tabs in the file
        
        # Adds edge as a list [tail, head] to the list
        edges.append([int(l[0]),int(l[1])])
        
        # Add vertices to list of vertices if not already in the list
        if int(edges[-1][0]) not in vertices:
            vertices.append(int(edges[-1][0]))
            explored[int(edges[-1][0])] = False
        if int(edges[-1][1]) not in vertices:
            vertices.append(int(edges[-1][1]))
            explored[int(edges[-1][1])] = False
    
    # Sorts vertices
    v_sorted = sorted(vertices)
    return v_sorted, edges, explored

time = 0
s = None

def depthFirstSearch1(v_list,e_list,node_i,finishing_time,explored):
    # gets called by depthFirstsearchLoop
    explored[node_i] = True
    for e in e_list:
        if e[0] == node_i:
            if not explored[e[1]]:
                depthFirstSearch1(v_list,e_list,e[1],finishing_time,explored)

    global time
    time += 1
    finishing_time[node_i] = time
    

def depthFirstSearchLoop1(v_list,e_list,finishing_time,explored):
    # gets called by depthFirstSearchMain
    for i in range(len(v_list) - 1,-1,-1):
        if not explored[v_list[i]]:
            depthFirstSearch1(v_list,e_list,v_list[i],finishing_time,explored)
        print("First search loop node: ",i)
    
    #for testing
    #print (finishing_time[1],finishing_time[2],finishing_time[3], finishing_time[4], finishing_time[5], finishing_time[6])
    
    
def depthFirstSearch2(v_list,e_list,node_i,leader,explored):
    global s
    explored[node_i] = True
    leader[s] += 1
    for e in e_list:
        if e[0] == node_i:
            if not explored[e[1]]:
                depthFirstSearch2(v_list,e_list,e[1],leader,explored)

def depthFirstSearchLoop2(v_list,e_list,leader,explored):
    global s
    for i in range(len(v_list) - 1,-1,-1):
        if not explored[v_list[i]]:
            leader[v_list[i]] = 0
            s = v_list[i]
            depthFirstSearch2(v_list,e_list,v_list[i],leader,explored)

def depthFirstSearchMain(v_list,e_list,explored):
    # define finishing time list, reverse graph, call the search twice here
    
    reverse_e_list = []
    for e in e_list:
        reverse_e_list.append([e[1],e[0]])
    
    finishing_time = {}
    depthFirstSearchLoop1(v_list,reverse_e_list,finishing_time,explored)
    
    # Resets explored dictionary and changes values of vertices to finishing times for second pass
    explored = {}
    leader = {}
    for v in v_list:
        v = finishing_time[v]
        explored[v] = False
        leader[v] = 0 # dictionary for number of nodes with v as the leader    
    v_list = sorted(v_list)
    
    #Reset edges to point at the correct vertices since vertex values changed to finishing time
    for e in e_list:
        e[0] = finishing_time[e[0]]
        e[1] = finishing_time[e[1]]
    
    print("Starting second pass")
    depthFirstSearchLoop2(v_list,e_list,leader,explored)
    
    #Find the 5 largest SCCs using frequency of nodes being the leader,
    #and print out their sizes
    
    values = list(leader.values())
    for i in range(5):
        highest = max(values)
        print((i+1), "th highest: ",highest)
        values.remove(highest)
    
def main(filename):
    file_object = open_file_to_read(filename)
    v_list,e_list,explored = read_from_file(file_object)
    close_file(file_object)
    print("File read")
  
    depthFirstSearchMain(v_list,e_list,explored)
    

#main("SCC.txt")
main("scc_test2.txt")
#main("test.txt")

