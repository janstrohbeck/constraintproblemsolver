from common import *
from constraint import Constraint
from utils import *
import itertools

class alldiff(Constraint):
    def __init__(self, touched_variables):
        Constraint.__init__(self, lambda variables: len([x for x in variables if len([y for y in variables if x == y]) > 1]) == 0, (touched_variables,))

    def forwardcheck(self, variables, variable_name, assignments):
        value = assignments[variable_name]
        for var_name in flatten(self.touched_variables):
            if var_name in assignments.keys():
                continue
            if var_name != variable_name:
                variables[var_name].domain.hide_value(value)
        return True

class same_house_constraint(Constraint):
    def __init__(self, variables1, value1, variables2, value2):
        Constraint.__init__(self, lambda vars1, vars2: len([i for i, val1 in enumerate(vars1) if val1 == value1 and vars2[i] == value2]) == 1, (variables1, variables2))
        self.value1 = value1
        self.value2 = value2

    def forwardcheck(self, variables, variable_name, assignments):
        value = assignments[variable_name]
        variables1, variables2 = self.touched_variables
        try:
            index_1 = variables1.index(variable_name)
            if value == self.value1:
                var_name = variables2[index_1]
                if var_name in assignments.keys():
                    return True
                variables[var_name].domain.hide_all_but(self.value2)
        except ValueError:
            try:
                index_2 = variables2.index(variable_name)
                if value == self.value2:
                    var_name = variables1[index_2]
                    if var_name in assignments.keys():
                        return True
                    variables[var_name].domain.hide_all_but(self.value1)
            except ValueError:
                pass
        return True


class next_to_constraint(Constraint):
    def __init__(self, variables1, value1, variables2, value2):
        Constraint.__init__(self, lambda vars1, vars2: abs(vars1.index(value1) - vars2.index(value2)) == 1, (variables1, variables2))
        self.value1 = value1
        self.value2 = value2

    def forwardcheck(self, variables, variable_name, assignments):
        value = assignments[variable_name]
        variables1, variables2 = self.touched_variables
        try:
            index_1 = variables1.index(variable_name)
            if value == self.value1:
                for i in itertools.chain(range(index_1-1), range(index_1+2,len(variables2))):
                    var_name = variables2[i]
                    if var_name in assignments.keys():
                        continue
                    variables[var_name].domain.hide_value(self.value2)
        except ValueError:
            try:
                index_2 = variables2.index(variable_name)
                if value == self.value2:
                    for i in itertools.chain(range(index_2-1), range(index_2+2,len(variables2))):
                        var_name = variables1[i]
                        if var_name in assignments.keys():
                            continue
                        variables[var_name].domain.hide_value(self.value1)
            except ValueError:
                pass
        return True


class right_of_constraint(Constraint):
    def __init__(self, variables1, value1, variables2, value2):
        Constraint.__init__(self, lambda vars1, vars2: vars1.index(value1) - vars2.index(value2) == 1, (variables1, variables2))
        self.value1 = value1
        self.value2 = value2

    def forwardcheck(self, variables, variable_name, assignments):
        value = assignments[variable_name]
        variables1, variables2 = self.touched_variables
        try:
            index_1 = variables1.index(variable_name)
            if value == self.value1:
                if index_1 == 0:
                    return False
                var_name = variables2[index_1-1]
                variables[var_name].domain.hide_all_but(self.value2)
            else:
                raise ValueError
        except ValueError:
            try:
                index_2 = variables2.index(variable_name)
                if value == self.value2:
                    if index_2 == len(variables2)-1:
                        return False
                    var_name = variables1[index_2+1]
                    variables[var_name].domain.hide_all_but(self.value1)
                else:
                    raise ValueError
            except ValueError:
                pass
        return True


class equals_value_constraint(Constraint):
    def __init__(self, variable, value):
        Constraint.__init__(self, lambda var: var == value, (variable,))


class exists_constraint(Constraint):
    def __init__(self, variables, value):
        Constraint.__init__(self, lambda vars: len([x for x in vars if x == value]) > 0, (variables,))


class variables_equal_constraint(Constraint):
    def __init__(self, variable1, variable2):
        Constraint.__init__(self, lambda var1, var2: var1 == var2, (variable1, variable2))


class diff_constraint(Constraint):
    def __init__(self, variable1, variable2, diff):
        Constraint.__init__(self, lambda var1, var2: var1 - var2 == diff, (variable1, variable2))


class absolute_diff_constraint(Constraint):
    def __init__(self, variable1, variable2, diff):
        Constraint.__init__(self, lambda var1, var2: abs(var1 - var2) == diff, (variable1, variable2))


class sum_modulo_ten_or_plus_one_constraint(Constraint):
    def __init__(self, variable1, variable2, variable3):
        Constraint.__init__(self, lambda var1, var2, var3: (var1 + var2) % 10 == var3 or (var1 + var2) % 10 + 1 == var3, (variable1, variable2, variable3))


class no_queens_check_constraint(Constraint):
    def __init__(self, variables):
        Constraint.__init__(self, lambda *values: len([row1 for name1, row1 in zip(variables, values) if \
        len([row2 for name2, row2 in zip(variables, values) if \
            row2 == row1 or \
            abs(name2 - name1) == abs(row2 - row1) \
        ]) != 1 \
    ]) == 0, variables)

    def forwardcheck(self, variables, variable_name, assignments):
        row = assignments[variable_name]
        col = variable_name
        for var_name in self.touched_variables:
            if not var_name in assignments.keys():
                col2 = var_name
                for row2 in variables[var_name].domain.possible_values[:]:
                    if row2 == row or abs(col2 - col) == abs(row2 - row):
                        variables[var_name].domain.hide_value(row2)
        return True


class exact_price_constraint(Constraint):
    def __init__(self, prices, variables, exact_price):
        Constraint.__init__(self, lambda *values: sum([num*prices[var] for var, num in zip(variables, values)]) == exact_price, variables)
