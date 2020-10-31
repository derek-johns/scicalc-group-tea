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
        current_value = int(memory.pop())
        new_value = decimal_conversion(new_mode, current_value)
        print("Your converted value is " + new_value + ". " + "\n")
        main_app.mode = new_mode
    else:
        print("That is not a valid mode.")


def decimal_conversion(to_mode, value):
    if to_mode == "decimal":
        new_value = str(value)
    elif to_mode == "binary": #has to be int
        new_value = bin(value)
    elif to_mode == "octal":
        new_value = oct(value)
    elif to_mode == "hexadecimal":
        new_value = hex(value)
    return new_value

"""
def binary_conversion(to_mode, value):
    if to_mode == "decimal": #has to be int
        value = str(value)
        #value = value[2:]
        print(value)
        new_value = int(value, 2)
    elif to_mode == "octal":
        new_value = oct(value)
    elif to_mode == "hexadecimal":
        new_value = hex(value)
    return new_value
"""

#switch_display_input("binary")