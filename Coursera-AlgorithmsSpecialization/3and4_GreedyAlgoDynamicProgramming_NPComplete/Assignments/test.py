import fileinput

def read_from_file(filename):
    """"""

    pairs_list = []

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) == 1:
            size = int(l[0])
            for i in range(0, size):
                pairs_list.append(set([]))
            print "finished making list"
        else:
            v1 = abs(int(l[0]))
            v2 = abs(int(l[1]))
            if v1 == 0 or v2 == 0:
                print "There is a zero in here somewhere"

            if v2 in pairs_list[v1 - 1] or v1 in pairs_list[v2 - 1]:
                print "pair %d and %d repeated in a clause" %(v1, v2)
            else:
                pairs_list[v1 - 1].add(v2)
                pairs_list[v2 - 1].add(v1)

    return

read_from_file("2sat1.txt")
print "done"
