from __future__ import print_function
from problem import Problem
from util_constraints import *
from constraintproblemsolver import ConstraintProblemSolver
from random import shuffle
import sys

def print_assignments(NUM_QUEENS, assignments):
    try:
        print("{0: <3} ".format(" "), end="")
        for col in range(NUM_QUEENS):
            print("{0: <3} ".format(col+1), end="")
        print()
        for row in range(NUM_QUEENS):
            print ("{0: <3} ".format(row+1), end="")
            for col in range(NUM_QUEENS):
                if assignments[col+1] == row+1:
                    print("{0: <3} ".format("Q"), end="")
                else:
                    print("{0: <3} ".format("x"), end="")
            print()
    except (TypeError, KeyError):
        print ("No Solution!")

if __name__ == "__main__":
    NUM_QUEENS = 8 if len(sys.argv) < 2 else int(sys.argv[1])

    variable_names = tuple(((i+1) for i in range(NUM_QUEENS)))

    constraints = [
        no_queens_check_constraint(variable_names)
    ]

    problem = Problem()
    for variable in variable_names:
        values = list(range(1, NUM_QUEENS+1))
        shuffle(values)
        problem.add_variable(variable, values)

    problem.add_constraints(constraints)

    solver = ConstraintProblemSolver(problem)
    assignments = solver.solve()
    if assignments != None:
        print("Failed Constraints: {}".format(problem.check_constraints(assignments)))
    print_assignments(NUM_QUEENS, assignments)

