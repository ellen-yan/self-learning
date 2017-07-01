# Coursera, Stanford Algorithms Specialization
# Course 1, Divide and Conquer
# Assignment 2
#
# Finding the number of inversions in an array inputed from a text file,
# where each row corresponds to an element in the array and the input
# contains only integers

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

def num_inversions(num_list):
    """Takes in a list of integers and returns the number of inversions
    in the list followed by the sorted list"""
    
    # base case
    if len(num_list) <= 1:
        return 0, num_list
    
    split_inv = 0
    sorted_list = []
    
    left_list = num_list[:int(len(num_list) / 2)]
    right_list = num_list[int(len(num_list) / 2):]
    
    # recursively calls itself to obtain number of inversions
    # within the left and right sides and the sorted left and right lists
    left_inv,sorted_left_list = num_inversions(left_list)
    right_inv,sorted_right_list = num_inversions(right_list)
    
    # counts the number of split inversions
    count = 0
    while sorted_left_list or sorted_right_list:

        if sorted_right_list and not sorted_left_list:
            sorted_list += sorted_right_list
            sorted_right_list = []
        elif sorted_left_list and not sorted_right_list:
            sorted_list += sorted_left_list
            sorted_left_list = []
        else:
            if sorted_left_list[0] <= sorted_right_list[0]:
                sorted_list.append(sorted_left_list[0])
                sorted_left_list = sorted_left_list[1:]
            else:
                sorted_list.append(sorted_right_list[0])
                sorted_right_list = sorted_right_list[1:]
                split_inv += len(sorted_left_list)
        
        count += 1

    return left_inv + right_inv + split_inv, sorted_list

def main(filename):
    # opens file and reads into file object and list
    file_object = open_file_to_read(filename)
    num_list = list_from_file(file_object)
    close_file(file_object)

    return num_inversions(num_list)[0]


def brute_force(filename):
    file_object = open_file_to_read(filename)
    num_list = list_from_file(file_object)
    close_file(file_object)
    
    total_inv = 0
    
    i = 0
    while i < len(num_list):
        j = i + 1
        while j < len(num_list):
            if num_list[j] < num_list[i]:
                total_inv += 1
            j += 1
        i += 1
    
    return total_inv

print(main("IntegerArray.txt"))
#print (brute_force("IntegerArray.txt"))