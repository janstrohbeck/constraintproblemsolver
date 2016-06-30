from __future__ import print_function
from problem import Problem
from util_constraints import *
from constraintproblemsolver import ConstraintProblemSolver
from operator import itemgetter

color_variable_names = (
    'red',
    'green',
    'white',
    'yellow',
    'blue'
)

nationality_variable_names = (
    'England',
    'Spain',
    'Ukraine',
    'Norway',
    'Japan'
)

pet_variable_names = (
    'Dog',
    'Snails',
    'Fox',
    'Horse',
    'Zebra'
)

drink_variable_names = (
    'Coffee',
    'Tea',
    'Milk',
    'Orange juice',
    'Water'
)

cigarette_variable_names = (
    'Atem-Gold',
    'Kools',
    'Chesterfield',
    'Lucky-Strike',
    'Parliaments'
)

def print_assignments(assignments):
    try:
        for variables in (color_variable_names, nationality_variable_names, pet_variable_names, drink_variable_names, cigarette_variable_names):
            for value, house in sorted([(key, assignments[key]) for key in variables], key=itemgetter(1)):
                print("{0:20} ".format(value), end='')
            print ("")
    except (TypeError, KeyError):
        print ("No Solution!")

constraints = [
    alldiff(color_variable_names),
    alldiff(nationality_variable_names),
    alldiff(pet_variable_names),
    alldiff(drink_variable_names),
    alldiff(cigarette_variable_names),
    variables_equal_constraint('England', 'red'),
    variables_equal_constraint('Spain', 'Dog'),
    variables_equal_constraint('Coffee', 'green'),
    variables_equal_constraint('Ukraine', 'Tea'),
    diff_constraint('green', 'white', 1),
    variables_equal_constraint('Atem-Gold', 'Snails'),
    variables_equal_constraint('Kools', 'yellow'),
    equals_value_constraint('Milk', 3),
    equals_value_constraint('Norway', 1),
    absolute_diff_constraint('Chesterfield', 'Fox', 1),
    absolute_diff_constraint('Kools', 'Horse', 1),
    variables_equal_constraint('Lucky-Strike', 'Orange juice'),
    variables_equal_constraint('Japan', 'Parliaments'),
    absolute_diff_constraint('Norway', 'blue', 1),
]

if __name__ == "__main__":
    problem = Problem()
    problem.add_variables(color_variable_names, range(1, 6))
    problem.add_variables(nationality_variable_names, range(1, 6))
    problem.add_variables(pet_variable_names, range(1, 6))
    problem.add_variables(drink_variable_names, range(1, 6))
    problem.add_variables(cigarette_variable_names, range(1, 6))

    problem.add_constraints(constraints)

    solver = ConstraintProblemSolver(problem)
    assignments = solver.solve()
    if assignments != None:
        print("Failed Constraints: {}".format(problem.check_constraints(assignments)))
    print_assignments(assignments)

