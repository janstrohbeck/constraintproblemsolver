from __future__ import print_function
from problem import Problem
from util_constraints import *
from constraintproblemsolver import ConstraintProblemSolver

variable_names = (
    "mixed_fruits",
    "french_fries",
    "side_salads",
    "hot_wings",
    "mozarella_sticks",
    "sampler_plates"
)

appetizer_prices = {
    "mixed_fruits": 2.15,
    "french_fries": 2.75,
    "side_salads": 3.35,
    "hot_wings": 3.55,
    "mozarella_sticks": 4.20,
    "sampler_plates": 5.80
}

TOTAL_PRICE = 15.05

def print_assignments(assignments):
    try:
        print(assignments)
        for key in sorted(assignments.keys()):
            print ("{} {}".format(assignments[key], key))
        print ("--------------------")
        print ("Total: {0: .2f}".format(sum([num*appetizer_prices[var] for var, num in assignments.items()])))
    except (TypeError, KeyError):
        print ("No Solution!")

constraints = [
    exact_price_constraint(appetizer_prices, variable_names, TOTAL_PRICE)
]

if __name__ == "__main__":
    problem = Problem()
    for variable in variable_names:
        values = list(range(0, int(TOTAL_PRICE/appetizer_prices[variable]+1)))
        problem.add_variable(variable, values)

    problem.add_constraints(constraints)

    solver = ConstraintProblemSolver(problem)
    assignments = solver.solve()
    if assignments != None:
        print("Failed Constraints: {}".format(problem.check_constraints(assignments)))
    print_assignments(assignments)

