# Coursera, Stanford Algorithms Specialization
# Course 1, Divide and Conquer
# Assignment 3
#
# Number of comparisons made by Quicksort with different pivots

def open_file_to_read(filename):
    int_file = open(filename,"r")
    return int_file

def close_file(file):
    file.close()

def list_from_file(file):
    """Takes a parameter file object with one integer per line and
    returns a list of these integers"""
    l = file.readlines()
    i = 0
    while i < len(l):
        l[i] = int(l[i])
        i += 1
    return l

# Compute the total number of comparisons used to sort the given input file
# by QuickSort. The number of comparisons depends on the elements
# chosen as pivots. Cound comparisons by adding m - 1 when there is a
# recursive call on a subarray of length m
#
# Part 1: Always choose first element as the pivot
# Part 2: Always choose the final element as the pivot
# (swap last and first elements before beginning partition subroutine)
# Part 3: Choose median number between first, median, and last numbers
# (do not count comparisons within this choice)

def getMedian(a, b, c):
    if a == max(a,b,c):
        return max(b,c)
    elif b == max(a,b,c):
        return max(a,c)
    return max(a,b)

# Assumes first element is the pivot and partitions from pos1 to pos2, inclusive
# Returns position of pivot
def partition(intarray, pos1, pos2):
    pivot = intarray[pos1]
    i = pos1
    j = i + 1
    while j <= pos2:
        if intarray[j] < pivot:
            temp = intarray[j]
            intarray[j] = intarray[i + 1]
            intarray[i + 1] = temp
            i += 1
        j += 1
        
    # swaps pivot and 
    temp = intarray[pos1]
    intarray[pos1] = intarray[i]
    intarray[i] = temp
    
    return i

# Swaps first and last elements (pos1 and pos2) - for part 2
def useFinalPivot(intarray, pos1, pos2):
    temp = intarray[pos1]
    intarray[pos1] = intarray[pos2]
    intarray[pos2] = temp

# Swaps first and the median value - for part 3
def useMedianPivot(intarray, pos1, pos2):
    med_pos = int((pos1 + pos2) / 2)
    
    median = getMedian(intarray[med_pos], intarray[pos1], intarray[pos2])
    if intarray[med_pos] == median:
        temp = intarray[med_pos]
        intarray[med_pos] = intarray[pos1]
        intarray[pos1] = temp
    elif intarray[pos2] == median:
        temp = intarray[pos2]
        intarray[pos2] = intarray[pos1]
        intarray[pos1] = temp

# This is for Part 1 of assignment. Sorts and returns number of comparisons made
# given array and elements from pos1 to pos2 inclusive, using
# first element as pivot
def quickSort1(intarray, pos1, pos2):
    # Base case
    if (pos2 - pos1) <= 0:
        return 0
    
    num_comparisons = pos2 - pos1
    pivot_pos = partition(intarray, pos1, pos2)
    left_comparisons = quickSort1(intarray, pos1, pivot_pos - 1)
    right_comparisons = quickSort1(intarray, pivot_pos + 1, pos2)
    
    return num_comparisons + left_comparisons + right_comparisons

# This is for Part 2 of the assignment. Sorts and returns number of comparisons
# made given array and elements from pos1 and pos2 inclusive, using
# final element as pivot
def quickSort2(intarray, pos1, pos2):
    # Base case
    if (pos2 - pos1) <= 0:
        return 0
    
    num_comparisons = pos2 - pos1
    useFinalPivot(intarray, pos1, pos2) # swap final and first elements
    pivot_pos = partition(intarray, pos1, pos2)
    left_comparisons = quickSort2(intarray, pos1, pivot_pos - 1)
    right_comparisons = quickSort2(intarray, pivot_pos + 1, pos2)
    
    return num_comparisons + left_comparisons + right_comparisons

def quickSort3(intarray, pos1, pos2):
    #Base case
    if (pos2 - pos1) <= 0:
        return 0
    
    num_comparisons = pos2 - pos1
    useMedianPivot(intarray, pos1, pos2) # swap first and the median-valued element
    pivot_pos = partition(intarray, pos1, pos2)
    left_comparisons = quickSort3(intarray, pos1, pivot_pos - 1)
    right_comparisons = quickSort3(intarray, pivot_pos + 1, pos2)
    
    return num_comparisons + left_comparisons + right_comparisons

def main(filename):
    # opens file and reads into file object and list
    file_object = open_file_to_read(filename)
    num_list = list_from_file(file_object)
    close_file(file_object)
    
    # Run the print statements below one at a time otherwise the array
    # will be modified and subsequent sorts would be performed
    # on the sorted list
    
    #print (quickSort1(num_list, 0, len(num_list) - 1))
    #print (quickSort2(num_list, 0, len(num_list) - 1))
    #print (quickSort3(num_list, 0, len(num_list) - 1))

main("QuickSort.txt")
