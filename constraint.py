from common import *

class Constraint:
    def __init__(self, constraint_f, touched_variables):
        self.constraint_f = constraint_f
        self.touched_variables = touched_variables

    def get_values(self, variable_names, assignments):
        result = []
        for var_name in variable_names:
            if type(var_name) == list or type(var_name) == tuple:
                res_ = self.get_values(var_name, assignments)
                if res_ == None:
                    return None
                result.append(res_)
            else:
                if not var_name in assignments.keys():
                    return None
                result.append(assignments[var_name])
        return result

    def evaluate(self, assignments):
        variable_values = self.get_values(self.touched_variables, assignments)
        if variable_values == None:
            return True
        try:
            return self.constraint_f(*variable_values)
        except ValueError:
            return False

    def forwardcheck(self, variables, variable_name, assignments):
        return True
