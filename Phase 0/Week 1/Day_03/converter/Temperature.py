# this class should be the base class for all other Temperature classes
# it should contain the following methods:
# 1. __init__(self, value, unit)
# 2. __repr__(self)
# it should contain the following attributes:
# 1. value
# 2. unit
# it should have the following constructors:

class Temperature:

    def __init__(self, value, unit: str):
        # declare given constructor arguments as object attributes
        self.value = float(value)
        self.unit = unit

    def __repr__(self):
        # return a string representation of the object
        return f"{self.value:.2f} {self.unit}"

