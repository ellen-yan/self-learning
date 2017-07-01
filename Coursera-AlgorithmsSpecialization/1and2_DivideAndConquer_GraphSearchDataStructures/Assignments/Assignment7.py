# Coursera, Stanford Algorithms Specialization
# Course 2, Graph Search
# Assignment 3
#
# Median Maintenance problem: given numbers one at a time,
# print the median from all the numbers given so far after each new number added

import fileinput

def medianMaintenance(filename):
    """Reads a file with one integer per line and computes the median after
    each entry"""

    median_list = [] # Stores all the medians calculated from each step

    heap_low = [] # heap of lower half of all input numbers; supports extract-max
    heap_high = [] # heap of higher half of all input numbers; supports extract-min

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        num = int(l[0])

        # General idea: add number to heap that makes the most sense
        # (by comparing against max of heap_low and min of heap_high), then
        # re-balance heaps at the end to make them even
        # For odd numbers, maintain one more element in the lower heap
        # so that median is consistently the maximum of the lower heap

        if len(heap_low) == 0 and len(heap_high) == 0:
            addToMaxHeap(heap_low, num) # First addition, both are empty

        elif len(heap_low) >= 1 and len(heap_high) == 0:
            if num > getRoot(heap_low):
                addToMinHeap(heap_high, num)
            else:
                addToMaxHeap(heap_low, num)
        else:
            # both heaps non-empty, compare num to max of lower heap and min of higher heap
            if num > getRoot(heap_high):
                # add to min heap
                addToMinHeap(heap_high, num)
            else:
                # add to max heap
                addToMaxHeap(heap_low, num)

        rebalanceHeaps(heap_low, heap_high)

        median_list.append(getRoot(heap_low))

    return median_list


def addToMaxHeap(heap, num):
    """A maximum heap maintained as a list, and an integer num to be added"""
    heap.append(num) # Adds number to last leaf

    if len(heap) == 1: # If heap is only the root, return
        return

    num_index = len(heap) - 1
    parent_index = (int((num_index + 1) / 2) - 1)

    while heap[num_index] > heap[parent_index] and num_index != 0:

        # Swap positions of parent and child
        temp = heap[num_index]
        heap[num_index] = heap[parent_index]
        heap[parent_index] = temp

        num_index = parent_index
        parent_index = int((num_index + 1) / 2) - 1


def addToMinHeap(heap, num):
    """A minimum heap maintained as a list, and an integer num to be added"""
    heap.append(num) # Adds number to last leaf

    if len(heap) <= 1: # If heap is only the root, return
        return

    num_index = len(heap) - 1
    parent_index = (int((num_index + 1) / 2) - 1)

    while heap[num_index] < heap[parent_index] and num_index != 0:

        # Swap positions of parent and child
        temp = heap[num_index]
        heap[num_index] = heap[parent_index]
        heap[parent_index] = temp

        num_index = parent_index
        parent_index = int((num_index + 1) / 2) - 1

def getRoot(heap):
    return heap[0]

def deleteMin(heap):
    # Deletes root from a minimum heap

    # Swap root and last element
    temp = heap[0]
    heap[0] = heap[-1]
    heap[-1] = temp

    root = heap.pop()

    if len(heap) <= 1:
        return root

    num_index = 0

    if len(heap) < 3:
        # swap child and parent and return
        temp = heap[0]
        heap[0] = heap[1]
        heap[1] = temp
        return root

    child_index1 = 1
    child_index2 = 2

    while (heap[num_index] > heap[child_index1] or heap[num_index] > heap[child_index2]):
        if child_index2 >= len(heap):
            child_index = child_index1
        else:
            if heap[child_index1] < heap[child_index2]:
                child_index = child_index1
            elif heap[child_index2] < heap[child_index1]:
                child_index = child_index2

        temp = heap[num_index]
        heap[num_index] = heap[child_index]
        heap[child_index] = temp

        num_index = child_index
        child_index1 = (num_index + 1) * 2 - 1
        child_index2 = (num_index + 1) * 2

        if child_index1 >= len(heap):
            return root
        elif child_index2 >= len(heap):
            # first child exists but second does not; only need to check the case when this child is not smaller than parent
            if heap[num_index] < heap[child_index1]:
                return root
    return root


def deleteMax(heap):
    # Deletes root from a maximum heap

    # Swap root and last element
    temp = heap[0]
    heap[0] = heap[-1]
    heap[-1] = temp

    root = heap.pop()

    if len(heap) <= 1:
        return root

    num_index = 0

    if len(heap) < 3:
        # swap child and parent and return
        temp = heap[0]
        heap[0] = heap[1]
        heap[1] = temp
        return root

    child_index1 = 1
    child_index2 = 2

    while heap[num_index] < heap[child_index1] or heap[num_index] < heap[child_index2]:

        if child_index2 >= len(heap):
            child_index = child_index1
        else:
            if heap[child_index1] > heap[child_index2]:
                child_index = child_index1
            elif heap[child_index2] > heap[child_index1]:
                child_index = child_index2

        temp = heap[num_index]
        heap[num_index] = heap[child_index]
        heap[child_index] = temp

        num_index = child_index
        child_index1 = (num_index + 1) * 2 - 1
        child_index2 = (num_index + 1) * 2

        if child_index1 >= len(heap):
            return root # neither of the two children exist
        elif child_index2 >= len(heap):
            # first child exists but second does not; only need to check the case when this child is not bigger than parent
            if heap[num_index] > heap[child_index1]:
                return root

    return root

def rebalanceHeaps(heap_max, heap_min):
    # Given two heaps, one a maximum heap and one a minimum heap, rebalances
    # heaps so that they contain the same number of elements differing at most by one
    # Input heaps never differ by more than 2 elements
    # Cases where nothing needs to be done:
    # 1) heap_max is larger than heap_min by one element
    # 2) sizes of two heaps are equal
    # Cases where one element needs to be moved:
    # 1) heap_min has one more element than heap_max --> move min element from heap_min to heap_max
    # 2) heap_max has two more elements than heap_min --> move max element from heap_max to heap_min

    if len(heap_max) == (len(heap_min) + 1) or len(heap_max) == len(heap_min):
        return

    if len(heap_min) == (len(heap_max) + 1):
        # Move min element from heap_min to heap_max
        num = deleteMin(heap_min)
        addToMaxHeap(heap_max, num)

    elif len(heap_max) == (len(heap_min) + 2):
        # Move max element from heap_max to heap_min
        num = deleteMax(heap_max)
        addToMinHeap(heap_min, num)

def main(filename):
    median_list = medianMaintenance(filename)

    # Ouput the last four digits of the sum of all the medians

    print(sum(median_list) % 10000)

main("Median.txt")
#main("test.txt")
