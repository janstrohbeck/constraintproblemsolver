from __future__ import print_function
from common import *
from utils import *

class ConstraintProblemSolver:
    def __init__(self, problem):
        self.problem = problem
        self.count = 0

    def get_unassigned_vars(self, assignments):
        unassigned_vars = []
        for var_name in self.problem.variables.keys():
            if not var_name in assignments.keys():
                unassigned_vars.append(var_name)
        return unassigned_vars

    def choose_unassigned_variable(self, assignments, unassigned_vars=None):
        global DEBUG_VERBOSITY
        if unassigned_vars == None:
            unassigned_vars = self.get_unassigned_vars(assignments)
        if len(unassigned_vars) == 0:
            return None
        if DEBUG_VERBOSITY > 1:
            print ([(key, self.problem.variables[key].domain.length()) for key in unassigned_vars])
        return min(unassigned_vars, key=lambda key: self.problem.variables[key].domain.length())

    def solve(self):
        def backtracking(problem, assignments={}):
            unassigned_vars = self.get_unassigned_vars(assignments)
            if len(unassigned_vars) == 0:
                if DEBUG_VERBOSITY > 1:
                    print("Found solution!")
                return assignments
            var_name = self.choose_unassigned_variable(assignments, unassigned_vars)
            if DEBUG_VERBOSITY > 1:
                print ('Choosing {}'.format(var_name))
            for val in problem.variables[var_name].domain.possible_values[:]:
                if FORWARD_CHECK:
                    for vn in problem.variables.keys():
                        problem.variables[vn].domain.push_state()
                self.count += 1
                if DEBUG_VERBOSITY > 0:
                    print ('Test {}: {} = {}'.format(self.count, var_name, val), end='')
                assignments[var_name] = val
                good = True
                if FORWARD_CHECK:
                    for constraint in problem.constraints:
                        if var_name in flatten(constraint.touched_variables):
                            if not constraint.forwardcheck(problem.variables, var_name, assignments):
                                good = False
                                break
                    if not good:
                        if DEBUG_VERBOSITY > 0:
                            print (" -> no good!")
                        for vn in problem.variables.keys():
                            problem.variables[vn].domain.pop_state()
                        continue
                failed_constraints = problem.check_constraints(assignments)
                if DEBUG_VERBOSITY > 0:
                    print (" -> {} failed constraints".format(failed_constraints))
                if failed_constraints == 0:
                    if DEBUG_VERBOSITY > 1:
                        print ('OK, Continuing with next variable')
                    res = backtracking(problem, assignments.copy())
                    if res != None:
                        return res
                if FORWARD_CHECK:
                    for vn in problem.variables.keys():
                        problem.variables[vn].domain.pop_state()
            if DEBUG_VERBOSITY > 1:
                print ('Backing up')
            return None
        return backtracking(self.problem)
