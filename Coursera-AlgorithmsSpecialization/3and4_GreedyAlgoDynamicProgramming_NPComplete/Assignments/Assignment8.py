# Coursera, Stanford Algorithms Specialization
# Course 4, Dynamic Programming, All Pairs Shortest Paths, NP Complete
# Assignment 2
# Python 2.7.10
#
# Solves the 2-SAT problem on six files using Papadimitriou's algorithm
# and determines which given files are solvable. In the input, a '-' indicates
# logical not, and the numbers indicate the variable number. For example,
# given "-23 4", means "not x23 or x4". Can assume that each pair of variables
# used in a clause appears as a pair at most once and variables cannot be a 0.
# Note that the variable numbers are not restricted to be below the number of
# clauses.

import fileinput
import random
import math

def read_from_file(filename):
    """Reads in a file containing a list of clauses for variables, where '-'
    denotes logical not, and variables are given as the variable number.
    Returns a list of clauses, where each clause is represented as a tuple,
    and a set of all variable names."""

    clauses_list = []
    variable_names_set = set()

    for line in fileinput.input([filename]):
        l = line.split() # list of strings, each a string separated from each other with tabs in the file
        if len(l) > 1:
            v1 = int(l[0])
            v2 = int(l[1])

            clauses_list.append((v1, v2))
            variable_names_set.add(v1)
            variable_names_set.add(v2)

    return clauses_list, variable_names_set

def clause_reduction(clauses_list, variable_names_set):
    """Given a list of clauses, iterates through all clauses and finds
    only those clauses where the positive and negation of variable exists
    in the list. Removes all other clauses where only positive or negative
    of that number exists. Returns a set of new variable names containing
    only those still present in the clauses."""

    clauses_after_reduction = set()
    new_variable_names_set = set()
    i = 0
    while i < len(clauses_list):
        v1 = clauses_list[i][0]
        v2 = clauses_list[i][1]
        if (v1 * -1) not in variable_names_set or (v2 * -1) not in variable_names_set:
            # remove clause
            clauses_list.pop(i)
        else:
            new_variable_names_set.add(v1)
            new_variable_names_set.add(v2)
            i += 1

    return new_variable_names_set

def generate_random_assignment(variable_names):
    """Given a set of variable names, assigns a random value True or False
    to each variable in a dictionary."""

    d = {}
    for name in variable_names:
        r = random.randint(0, 1)
        if r == 0:
            d[abs(name)] = False
        else:
            d[abs(name)] = True
    return d

def check_satisfied(clauses_list, assignment_dict):
    """Given a list of clauses as tuples, checks whether the current
    assignments (given in assignment_dict) fulfills all clauses.
    Returns None if all clauses were satisfied, otherwise returns a random
    clause which is not satisfied as a tuple."""

    satisfied = True # whether all clauses are satisifed
    unsatisfied_clauses_set = set()

    for clause in clauses_list:
        v1 = clause[0]
        v2 = clause[1]
        # less than 0 --> NOT var, should be assigned False

        evaluated_clause = False
        if v1 < 0 and v2 < 0:
            if not assignment_dict[abs(v1)] or not assignment_dict[abs(v2)]:
                evaluated_clause = True
        elif v1 < 0 and v2 > 0:
            if not assignment_dict[abs(v1)] or assignment_dict[abs(v2)]:
                evaluated_clause = True
        elif v1 > 0 and v2 < 0:
            if assignment_dict[abs(v1)] or not assignment_dict[abs(v2)]:
                evaluated_clause = True
        elif v1 > 0 and v2 > 0:
            if assignment_dict[abs(v1)] or assignment_dict[abs(v2)]:
                evaluated_clause = True
        else:
            print "You shouldn't be here"

        # Clause is not fulfilled, satisfied = False and add clause to
        # list of unsatisfied clauses
        if not evaluated_clause:
            # clause is not satisfied
            satisfied = False
            unsatisfied_clauses_set.add(clause)

    if satisfied:
        return None
    else:
        # returns a list of the sampled tuples
        r = random.sample(unsatisfied_clauses_set, 1)
        return r[0]

def papadimitriou_2sat(clauses_list, variable_names_set):
    """Given a list of clauses as outputted by the read_from_file function
    and an assignment list of True or False at each position i for variable
    i + 1, attempts to find an assignment that satisfies all clauses and
    returns True if an assignment can be found, False otherwise."""
    num_iterations = int(math.log(len(variable_names_set), 2))
    i = 0
    while i <= num_iterations:
        assignment_dict = generate_random_assignment(variable_names_set)
        num_iterations2 = 2 * (len(variable_names_set)) # should be 2(n^2), here only 2n for time
        j = 0
        while j <= num_iterations2:
            # if current assignment satisfies all clauses, halt and return True
            # else, pick arbitrary unsatisfied clause and flip the value
            # of one of its variables uniformly at random
            tup_to_change = check_satisfied(clauses_list, assignment_dict)
            if tup_to_change == None:
                return True, assignment_dict

            # change one of the assignments to the opposite
            r = random.randint(0, 1)
            var = abs(tup_to_change[r])
            if assignment_dict[var]:
                assignment_dict[var] = False
            else:
                assignment_dict[var] = True

            if j % 100 == 0:
                print "Finished %d iterations out of %d" % (j, num_iterations2)

            j += 1

        i += 1

        print "Finished iteration %d out of %d" % (i, num_iterations)

    # all iterations completed, no satisfying condition found
    return False, {}


def main(filename):
    clauses_list, variable_names_set = read_from_file(filename)
    variable_names_set = clause_reduction(clauses_list, variable_names_set)
    #print clauses_list
    print "Finished reading file and reducing clauses to %d..." % len(clauses_list)
    satisfied, assignment_dict = papadimitriou_2sat(clauses_list, variable_names_set)
    print "Found assignment that satisfies all clauses:", satisfied, "\a"
    #print assignment_dict



#main("2sat1.txt")
#main("2sat2.txt")
#main("2sat3.txt")
main("2sat4.txt")
#main("2sat5.txt")
#main("2sat6.txt")
#main("test.txt")
