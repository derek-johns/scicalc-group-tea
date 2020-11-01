import math
import calculator as calc

def switch_display_list(mode):
    print("You are in " + mode)
    modes = ["decimal", "hexadecimal", "binary", "octal"]
    index = modes.index(mode)

def switch_display_input(mode):
    import importlib
    main_app = importlib.import_module("main-app")

    print("You are in " + mode)
    new_mode = input("Input a new mode. \n")
    modes = ["decimal", "hexadecimal", "binary", "octal"]
    if new_mode in modes:
        print("You have switched to " + new_mode + ".")
        memory = main_app.m
        current_value = int(memory[-1])
        new_value = str(decimal_conversion(new_mode, current_value))
        main_app.mode = new_mode
        if new_mode != "decimal":
            new_value = str(new_value)
            new_value = new_value[2:]
        print(new_value)
    else:
        print("That is not a valid mode.")


def decimal_conversion(to_mode, value):
    if to_mode == "decimal":
        new_value = str(value)
    elif to_mode == "binary":
        new_value = bin(value)
    elif to_mode == "octal":
        new_value = oct(value)
    elif to_mode == "hexadecimal":
        new_value = hex(value)
    return new_value

def switch_units_input(mode):
    import importlib
    main_app = importlib.import_module("main-app")

    print("You are in " + mode)
    new_mode = input("Input a new mode. \n")
    if new_mode == "degrees" or new_mode == "radians":
        print("You have switched to " + new_mode + ".")
        memory = main_app.m
        current_value = memory[-1]
        new_value = angle_conversion(new_mode, current_value)
        print("Your converted value is " + str(new_value) + ". " + "\n")
        main_app.mode_ang = new_mode
    else:
        print("That is not a valid mode.")

def angle_conversion(to_mode, value):
    if to_mode == "degrees":
        new_value = round(value * 180/math.pi, 2)
    elif to_mode == "radians":
        new_value = round(value * math.pi/180, 4)
    else:
        print("Cannot convert")
    return new_value
