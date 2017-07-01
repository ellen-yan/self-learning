def print_num(highest, increment):
    i = 0
    numbers = []
    while i < highest:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


print "The numbers: "
numbers = print_num(6, 1)
for num in numbers:
    print num
