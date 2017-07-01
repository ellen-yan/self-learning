# Coursera, Stanford Algorithms Specialization
# Course 3, Greedy Algorithms
# Assignment 1, Part 2 of 3
#
# Part 2: Given the same file as part 1, schedule jobs in decreasing order of
# the ratio (weight/length) (doesn't matter how ties are broken) and report
# sum of weighted completion times of the resulting schedule

import fileinput

def read_from_file(filename):
    """For Part 2: Reads a file containing job weight and lengths and outputs
    a dictionary mapping the job number to their weight/length, weight, and length"""
    
    job_dict = {} # maps the job number to the list [weight - length,weight,length] of job
    ratio_list = []
    i = 0
    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) != 1:
            i += 1
            weight = int(l[0])
            length = int(l[1])
            job_dict[i] = [weight/length, weight, length]
            ratio_list.append(weight/length)
        
    ratio_list = sorted(ratio_list)
    
    return job_dict, ratio_list

def schedule(job_dict, ratio_list):
    # calculate the sum of weighted completion times for jobs scheduled in order
    # of decreasing ratio (i.e. end of list ratio_list, a sorted list of weight/length)
    
    completion_time = 0
    sum_of_weighted = 0
    
    while job_dict:
        ratio = ratio_list.pop()
        next_key = -1
        # Find the next element in the job to remove (schedule)
        for key in job_dict:
            if job_dict[key][0] == ratio:
                next_key = key
                break
                
        completion_time += job_dict[next_key][2]
        sum_of_weighted += job_dict[next_key][1] * completion_time
        
        del job_dict[next_key]
    
    return sum_of_weighted


def main(filename):
    job_dict,ratio_list= read_from_file(filename)
    print(schedule(job_dict,ratio_list))
    print(job_dict)
    print("done")

main("jobs.txt")