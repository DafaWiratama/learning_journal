# import Base Temperature class from Implementing inheritance
from .Temperature import Temperature


# this function bellow should be used to convert temperature from one unit to another
# it should take one argument which is the temperature to be converted
# it should return the converted temperature
# should be able to convert from celsius, fahrenheit, kelvin
# should be able to convert to celsius, fahrenheit, kelvin

# formula for celsius to fahrenheit
# (°C × 9/5) + 32 = °F
def celsius_to_fahrenheit(value):
    return value * 1.8 + 32


# formula for celsius to kelvin
# (°C + 273.15) = K
def celsius_to_kelvin(value):
    return value + 273.15


# formula for fahrenheit to celsius
# (°F − 32) × 5/9 = °C
def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9


# formula for fahrenheit to kelvin
# ((°F − 32) × 5/9) + 273.15 = K
def fahrenheit_to_kelvin(value):
    return (value - 32) * 5 / 9 + 273.15


# formula for kelvin to celsius
# (K − 273.15) = °C
def kelvin_to_celsius(value):
    return value - 273.15


# formula for kelvin to fahrenheit
# ((K − 273.15) × 9/5) + 32 = °F
def kelvin_to_fahrenheit(value):
    return value * 9 / 5 - 459.67


# this class bellow should be implementing Base Temperature Class and should have method to convert temperature

class Celsius(Temperature):

    def __init__(self, value):
        # this line should be used to call the __init__ method of the Base Temperature Class and passing value and unit as argument/parameter
        super().__init__(value, "°C")

    def to_fahrenheit(self):
        # call the celsius_to_fahrenheit function and pass the value of the temperature
        return Fahrenheit(celsius_to_fahrenheit(self.value))

    def to_kelvin(self):
        # call the celsius_to_kelvin function and pass the value of the temperature
        return Kelvin(celsius_to_kelvin(self.value))


# this class should implement same as above but for kelvin
class Kelvin(Temperature):

    def __init__(self, value):
        super().__init__(value, "°K")

    def to_celsius(self):
        return Celsius(kelvin_to_celsius(self.value))

    def to_fahrenheit(self):
        return Fahrenheit(kelvin_to_fahrenheit(self.value))


# this class should implement same as above but for fahrenheit
class Fahrenheit(Temperature):

    def __init__(self, value):
        super().__init__(value, "°F")

    def to_celsius(self):
        return Celsius(fahrenheit_to_celsius(self.value))

    def to_kelvin(self):
        return Kelvin(fahrenheit_to_kelvin(self.value))
