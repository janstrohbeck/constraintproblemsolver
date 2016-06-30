from common import *

class VariableDomain:
    def __init__(self, possible_values):
        self.possible_values = list(possible_values[:])
        self.hidden_values = []
        self.states = []

    def hide_value(self, value):
        try:
            self.possible_values.remove(value)
            self.hidden_values.append(value)
        except ValueError:
            pass

    def hide_all(self):
        for val in self.possible_values[:]:
            self.hide_value(val)

    def hide_all_but(self, value):
        for val in self.possible_values[:]:
            if val != value:
                self.hide_value(val)

    def push_state(self):
        self.states.append(len(self.possible_values))

    def pop_state(self):
        diff = self.states.pop()-len(self.possible_values)
        if diff > 0:
            self.possible_values.extend(self.hidden_values[-diff:])
            del self.hidden_values[-diff:]

    def length(self):
        return len(self.possible_values)

class Variable:
    def __init__(self, name, possible_values):
        self.name = name
        self.domain = VariableDomain(possible_values)

    def __repr__(self):
        return self.name
