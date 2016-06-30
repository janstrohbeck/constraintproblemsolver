from __future__ import print_function
from problem import Problem
from util_constraints import *
from constraintproblemsolver import ConstraintProblemSolver

variable_names = (
    'S',
    'E',
    'N',
    'D',
    'M',
    'O',
    'R',
    'Y'
)

def print_assignments(assignments):
    try:
        print ("    {S}{E}{N}{D}".format(**assignments))
        print ("  + {M}{O}{R}{E}".format(**assignments))
        print ("   -----".format(**assignments))
        print (" = {M}{O}{N}{E}{Y}".format(**assignments))
    except (TypeError, KeyError):
        print ("No Solution!")

constraints = [
    alldiff(variable_names),
    sum_modulo_ten_or_plus_one_constraint('D', 'E', 'Y'),
    sum_modulo_ten_or_plus_one_constraint('N', 'R', 'E'),
    sum_modulo_ten_or_plus_one_constraint('E', 'O', 'N'),
    sum_modulo_ten_or_plus_one_constraint('S', 'M', 'O'),
    Constraint(lambda s, e, n, d, m, o, r, y: 1000*s + 100*e + 10*n + d + 1000*m + 100*o + 10*r + e == 10000*m + 1000*o + 100*n + 10*e + y, ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'))
]

if __name__ == "__main__":
    problem = Problem()
    problem.add_variables(('S',), range(0, 10))
    problem.add_variables(('E',), range(0, 10))
    problem.add_variables(('N',), range(0, 10))
    problem.add_variables(('D',), range(0, 10))
    problem.add_variables(('M',), range(1, 10))
    problem.add_variables(('O',), range(0, 10))
    problem.add_variables(('R',), range(0, 10))
    problem.add_variables(('Y',), range(0, 10))

    problem.add_constraints(constraints)

    solver = ConstraintProblemSolver(problem)
    assignments = solver.solve()
    if assignments != None:
        print("Failed Constraints: {}".format(problem.check_constraints(assignments)))
    print_assignments(assignments)

