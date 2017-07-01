# Coursera, Stanford Algorithms Specialization
# Course 2, Graph Search
# Assignment 4
#
# 2-SUM algorithm: given an array of integers (negative or positive and can
# have repetitions), compute the number of target values t in the interval
# [-10000,10000] (inclusive) such that there are *distinct* numbers x, y 
# in the input that satisfy x + y = t.

import fileinput

def read_from_file(filename):
    """Reads a file with one integer per line"""
    int_set = set()
    int_list = [] # for iterable with no duplicates
    
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        num = int(l[0])
        if num not in int_set:
            int_list.append(num)
            int_set.add(num)
    
    return int_set, int_list

def twoSum(int_set, int_list, lower_bound, upper_bound): # inclusive lower and upper bounds
    
    num_sums = 0
    
    target = lower_bound - 1
    while target < upper_bound: # loops through target values from lower_bound to upper_bound inclusive
        target += 1
        for i in int_list:
            # for each non-duplicate integer, look for the remainder target - i
            # that complements i, and break out of loop if found and remainder and i are distinct, adding one to number of targets
            # that can be achieved with numbers in the list
            remainder = target - i
            if remainder in int_set and remainder != i:
                num_sums += 1
                print ("found: ", i, remainder)
                break
        if target % 10 == 0:
            print("target done: ",target, "num_sums: ", num_sums)
            
    return num_sums


def main(filename):
    int_set, int_list = read_from_file(filename)
    print("file read")
    
    num_sums = twoSum(int_set, int_list, -10000, 10000) # number of distinct integer pairs in int_set with sums between last two arguments
    print(num_sums)


main("algo1-programming_prob-2sum.txt")
#main("test.txt")