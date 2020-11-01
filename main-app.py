from calculator import Calculator
import sys
import menu
import switch_mode as switch

m = [0]
m1 = [0]
display = 0
mode = "decimal"
mode_ang = "radians"

def getOneNumber():
    a = input("number? ")
    a = check_memory_function(a)
    try:
        c = float(a)
        return c
    except ValueError:
        print("Error!")
        menu.run_menu()

def getTwoNumbers():
    a = input("first number? ")
    b = input("second number? ")
    a = check_memory_function(a)
    b = check_memory_function(b)
    try:
        c = float(a)
        d = float(b)
        return c, d
    except ValueError:
        print("Error!")
        menu.run_menu()

def check_memory_function(value_to_check):
    if value_to_check == "MRC":
        return m1[0]
    else:
        return value_to_check

def displayResult(x: float):
    if type(x) == str and (x[:2] == "0b" or x[:2] == "0x" or x[:2] == "0o"):
        x_p = x[2:]
        print(x_p, "\n")
        m.append(x)
    elif type(x) == str:
            print(x, "\n")
    elif x % 1 != 0 or (x % 1 == 0 and mode == "decimal"):
        x = round(x, 4)
        print(x, "\n")
        m.append(x)
    elif x % 1 == 0 and mode != "decimal":
        original = x
        x = switch.decimal_conversion(mode, int(x))
        x_p = x[2:]
        print(mode)
        print(x_p, "\n")
        m.append(original)
    return m

def performCalcLoop():
    print("Welcome to the calculator")
    print("Type MRC at any time when being asked for number to recall a value that you saved to memory.")
    while True:
        result = menu.run_menu()
        if result == "exit":
            break

# main start
def main():
    performCalcLoop()
    print("Done Calculating.")


if __name__ == '__main__':
    main()
