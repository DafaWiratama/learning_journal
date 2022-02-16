# import converter module into current file
from converter import *


# this function should check if the conversion calculation is correct
def on_sanity_check():
    # define starting conditions with known values
    celsius = Celsius(100)
    fahrenheit = Fahrenheit(100)
    kelvin = Kelvin(100)

    # print all celsius class conversion for manual inspection
    print("Should return 100°C : ", celsius)
    print("Should return 212°F when converting from 100°C to °F : ", celsius.to_fahrenheit())
    print("Should return 373.15°K when converting from 100°C to °K : ", celsius.to_kelvin())
    print("")

    # print all fahrenheit class conversion for manual inspection
    print("Should return 100°F : ", fahrenheit)
    print("Should return 37.78°C when converting from 100°F to °C : ", fahrenheit.to_celsius())
    print("Should return 310.93°K when converting from 100°F to °K : ", fahrenheit.to_kelvin())
    print("")

    # print all kelvin class conversion for manual inspection
    print("Should return 100°K : ", kelvin)
    print("Should return -173.15°C when converting from 100°K to °C : ", kelvin.to_celsius())
    print("Should return -279.67°F when converting from 100°K to °F : ", kelvin.to_fahrenheit())

    # this should perform automated test from the given test cases with known values
    assert celsius.to_fahrenheit().value == 212
    assert celsius.to_kelvin().value == 373.15

    assert fahrenheit.to_celsius().value == 37.77777777777778
    assert fahrenheit.to_kelvin().value == 310.92777777777775

    assert kelvin.to_celsius().value == -173.14999999999998
    assert kelvin.to_fahrenheit().value == -279.67


# this function should ask user for input and convert it to another unit
def on_user_input():
    # start input loop
    while True:
        # start with asking user for input until they choose to quit
        # print prompt to input a temperature value followed by the unit
        print("Enter a temperature in given format ###.## C/F/K")
        user_input = input(">>> ")

        # if user not input anything, quit the program
        if user_input == "":
            break

        # perform try-except block to catch any error
        try:
            # split user input into 2 parts
            # 1. Temperature Value
            # 2. Temperature Unit
            user_input = user_input.split(" ")
            value = user_input[0]
            unit = user_input[1].lower()

            # convert user input to correct type
            # with nested if logic
            if unit == "c":
                source = Celsius(value)
            elif unit == "f":
                source = Fahrenheit(value)
            elif unit == "k":
                source = Kelvin(value)
            else:
                print("Invalid unit")
                continue
        # should catch any exception from try block
        except IndexError as _:
            print("Invalid input")
            continue
        except Exception as e:
            # if any error occurs, print error message and exit application
            return print(f"Some error has occurred with following stacktrace :{e}")

        # perform logic checking for conversion we will not show same unit as input
        if not isinstance(source, Celsius):
            print("Celsius : ", source.to_celsius())
        if not isinstance(source, Fahrenheit):
            print("Fahrenheit : ", source.to_fahrenheit())
        if not isinstance(source, Kelvin):
            print("Kelvin : ", source.to_kelvin())

        # prompt user to input again or quit
        print("Convert another temperature? (y/n)")
        user_input = input(">>> ")
        if user_input == "n":
            break


# this function should run the program routine
def on_runtime():
    # prompt user to choose to perform sanity check or not
    if input("Sanity check? (y/N) :") == "y":
        on_sanity_check()

    # prompt user to choose to perform user input or not
    if input("User input? (y/N) :") == "y":
        on_user_input()


# run the routine
on_runtime()
