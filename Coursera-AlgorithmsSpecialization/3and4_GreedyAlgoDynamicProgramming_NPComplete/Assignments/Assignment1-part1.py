# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 1, Part 1 of 3
#
# Part 1: Given a list of job weights and lengths, compute the sum of
# weighted completion times from a schedule that consists of
# jobs in decreasing order of the difference (weight - length), with the higher
# weight first if tied.

import fileinput

def read_from_file(filename):
    """For Part 1: Reads a file containing job weight and lengths and outputs
    a dictionary mapping the job number to their weight - length, weight, and length"""
    
    job_dict = {} # maps the job number to the list [weight - length,weight,length] of job
    difference_list = []
    i = 0
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) != 1:
            i += 1
            weight = int(l[0])
            length = int(l[1])
            job_dict[i] = [weight - length, weight, length]
            difference_list.append(weight - length)
    
    difference_list = sorted(difference_list)
    
    return job_dict, difference_list

def schedule(job_dict, difference_list):
    # calculate the sum of weighted completion times for jobs scheduled in order
    # of decreasing difference (i.e. end of list difference_list, a sorted list of weight - length)
    
    completion_time = 0
    sum_of_weighted = 0
    
    while job_dict:
        diff = difference_list.pop()
        next_key = -1        
        # Find the next element in the job to remove (schedule)
        for key in job_dict:
            if job_dict[key][0] == diff:
                if next_key == -1:
                    next_key = key
                elif job_dict[next_key][1] < job_dict[key][1]:
                    next_key = key
                
        completion_time += job_dict[next_key][2]
        sum_of_weighted += job_dict[next_key][1] * completion_time
        
        del job_dict[next_key]
    
    return sum_of_weighted

def main(filename):
    job_dict,difference_list = read_from_file(filename)
    print(schedule(job_dict,difference_list))
    print(job_dict)
    print("done")

main("jobs.txt")