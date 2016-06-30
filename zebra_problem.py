from __future__ import print_function
from problem import Problem
from util_constraints import *
from constraintproblemsolver import ConstraintProblemSolver

color_variable_names = (
    "house1color",
    "house2color",
    "house3color",
    "house4color",
    "house5color"
)

color_variable_values = (
    'red',
    'green',
    'white',
    'yellow',
    'blue'
)

nationality_variable_names = (
    "house1nationality",
    "house2nationality",
    "house3nationality",
    "house4nationality",
    "house5nationality"
)

nationality_variable_values = (
    'England',
    'Spain',
    'Ukraine',
    'Norway',
    'Japan'
)

pet_variable_names = (
    "house1pet",
    "house2pet",
    "house3pet",
    "house4pet",
    "house5pet"
)

pet_variable_values = (
    'Dog',
    'Snails',
    'Fox',
    'Horse',
    'Zebra'
)

drink_variable_names = (
    "house1drink",
    "house2drink",
    "house3drink",
    "house4drink",
    "house5drink"
)

drink_variable_values = (
    'Coffee',
    'Tea',
    'Milk',
    'Orange juice',
    'Water'
)

cigarette_variable_names = (
    "house1cigarette",
    "house2cigarette",
    "house3cigarette",
    "house4cigarette",
    "house5cigarette"
)

cigarette_variable_values = (
    'Atem-Gold',
    'Kools',
    'Chesterfield',
    'Lucky-Strike',
    'Parliaments'
)

def print_assignments(assignments):
    try:
        print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(
            assignments["house1color"],
            assignments["house2color"],
            assignments["house3color"],
            assignments["house4color"],
            assignments["house5color"]))
        print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(
            assignments["house1nationality"],
            assignments["house2nationality"],
            assignments["house3nationality"],
            assignments["house4nationality"],
            assignments["house5nationality"]))
        print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(
            assignments["house1pet"],
            assignments["house2pet"],
            assignments["house3pet"],
            assignments["house4pet"],
            assignments["house5pet"]))
        print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(
            assignments["house1drink"],
            assignments["house2drink"],
            assignments["house3drink"],
            assignments["house4drink"],
            assignments["house5drink"]))
        print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(
            assignments["house1cigarette"],
            assignments["house2cigarette"],
            assignments["house3cigarette"],
            assignments["house4cigarette"],
            assignments["house5cigarette"]))
    except (TypeError, KeyError):
        print ("No Solution!")

constraints = [
    alldiff(color_variable_names),
    alldiff(nationality_variable_names),
    alldiff(pet_variable_names),
    alldiff(drink_variable_names),
    alldiff(cigarette_variable_names),
    same_house_constraint(color_variable_names, 'red', nationality_variable_names, 'England'),
    same_house_constraint(nationality_variable_names, 'Spain', pet_variable_names, 'Dog'),
    same_house_constraint(drink_variable_names, 'Coffee', color_variable_names, 'green'),
    same_house_constraint(nationality_variable_names, 'Ukraine', drink_variable_names, 'Tea'),
    right_of_constraint(color_variable_names, 'green', color_variable_names, 'white'),
    same_house_constraint(cigarette_variable_names, 'Atem-Gold', pet_variable_names, 'Snails'),
    same_house_constraint(cigarette_variable_names, 'Kools', color_variable_names, 'yellow'),
    equals_value_constraint('house3drink', 'Milk'),
    equals_value_constraint('house1nationality', 'Norway'),
    next_to_constraint(cigarette_variable_names, 'Chesterfield', pet_variable_names, 'Fox'),
    next_to_constraint(cigarette_variable_names, 'Kools', pet_variable_names, 'Horse'),
    same_house_constraint(cigarette_variable_names, 'Lucky-Strike', drink_variable_names, 'Orange juice'),
    same_house_constraint(nationality_variable_names, 'Japan', cigarette_variable_names, 'Parliaments'),
    next_to_constraint(nationality_variable_names, 'Norway', color_variable_names, 'blue'),
    #exists_constraint(drink_variable_names, 'Water'),
    #exists_constraint(pet_variable_names, 'Zebra')
]

if __name__ == "__main__":
    problem = Problem()
    problem.add_variables(color_variable_names, color_variable_values)
    problem.add_variables(nationality_variable_names, nationality_variable_values)
    problem.add_variables(pet_variable_names, pet_variable_values)
    problem.add_variables(drink_variable_names, drink_variable_values)
    problem.add_variables(cigarette_variable_names, cigarette_variable_values)

    problem.add_constraints(constraints)

    solver = ConstraintProblemSolver(problem)
    assignments = solver.solve()
    if assignments != None:
        print("Failed Constraints: {}".format(problem.check_constraints(assignments)))
    print_assignments(assignments)
