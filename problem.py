from common import *
from variables import Variable

class Problem:
    def __init__(self):
        self.variables = {}
        self.constraints = []

    def add_variable(self, variable_name, possible_values):
        self.variables[variable_name] = Variable(variable_name, possible_values)

    def add_variables(self, variable_names, possible_values):
        for var_name in variable_names:
            self.add_variable(var_name, possible_values)

    def add_constraints(self, constraints):
        self.constraints.extend(constraints)

    def check_constraints(self, assignments):
        # res = 0
        # for i, constraint in enumerate(self.constraints):
        #     if not constraint.evaluate(assignments):
        #         print ("Constraint {} failed".format(i))
        #         res += 1
        # return res
        return len([True for constraint in self.constraints if not constraint.evaluate(assignments)])
