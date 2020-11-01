#changing to main_app.py for import
import importlib
main_app = importlib.import_module("main-app")
import switch_mode
from calculator import Calculator

calc = Calculator()

path = []

def start_menu(path):
    operation = input("Perform a \n [1] Basic Functionality \n "
                      "[2] Simple Operations \n "
                      "[3] Scientific Operations \n "
                      "[4] Complex Operations \n [5] Exit \n")
    path.append(operation)
    result = "good"
    if operation == "1":
        basics(path)
    elif operation == "2":
        simple(path)
    elif operation == "3":
        scientific(path)
    elif operation == "4":
        complex(path)
    elif operation == "5":
        result = "exit"
    else:
        print("Enter a valid input.")
        run_menu()
    return result

def basics(path):
    print("Basic Functionality")
    operation1 = input(" [1] Display value \n [2] Clear display \n "
                       "[3] Absolute value \n [4] Floor \n [5] Ceiling \n "
                       "[6] Add value to memory \n [7] Clear memory \n "
                       "[8] Recall value in memory \n "
                       "[9] Switch display by input \n "
                       "[10] Switch units by input \n "
                       "[11] Back \n" )
    path.append(operation1)
    if operation1 == "1":
        memory = main_app.m
        current_value = memory.pop()
        print(current_value)
    elif operation1 == "2":
        print(0)
    elif operation1 == "3":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.absolute_value(a))
    elif operation1 == "4":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.floor(a))
    elif operation1 == "5":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.ceil(a))
    elif operation1 == "6":
        calc.m_plus(main_app.m, main_app.m1)
    elif operation1 == "7":
        calc.m_reset(main_app.m, main_app.m1)
    elif operation1 == "8":
        calc.m_recall(main_app.m1)
    elif operation1 == "9":
        switch_mode.switch_display_input(main_app.mode)
    elif operation1 == "10":
        switch_mode.switch_units_input(main_app.mode_ang)
    elif operation1 == "11":
        back(path)
    else:
        print("Enter a valid input.")

def simple(path):
    print("Simple Operations")
    operation2 = input(" [1] Add \n [2] Subtract \n [3] Multiply \n "
                       "[4] Divide \n [5] Square \n [6] Square Root \n "
                       "[7] Exponential \n [8] Inverse \n "
                       "[9] Change sign \n [10] Back \n")
    path.append(operation2)
    if operation2 == "1":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.add(a,b))
    elif operation2 == "2":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.sub(a,b))
    elif operation2 == "3":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.mul(a,b))
    elif operation2 == "4":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.div(a,b))
    elif operation2 == "5":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.sqr(a))
    elif operation2 == "6":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.sqroot(a))
    elif operation2 == "7":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.exponentiation(a, b))
    elif operation2 == "8":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.inverse(a))
    elif operation2 == "9":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.invert_sign(a))
    elif operation2 == "10":
        back(path)
    else:
        print("Enter a valid input." + "\n")

def scientific(path):
    print("Scientific Operations")
    operation3 = input(" [1] Sine \n [2] Cosine \n [3] Tangent \n "
                       "[4] Inverse Sine \n [5] Inverse Cosine \n "
                       "[6] Inverse Tangent \n [7] Back \n")
    path.append(operation3)
    if operation3 == "1":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.sine(a, main_app.mode_ang))
    elif operation3 == "2":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.cosine(a,  main_app.mode_ang))
    elif operation3 == "3":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.tangent(a,  main_app.mode_ang))
    elif operation3 == "4":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.inverse_sine(a))
    elif operation3 == "5":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.inverse_cosine(a))
    elif operation3 == "6":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.inverse_tan(a))
    elif operation3 == "7":
        back(path)
    else:
        print("Enter a valid input.")

def complex(path):
    print("Complex Operations")
    operation4 = input(" [1] Factorial \n [2] Logarithm \n "
                       "[3] Inverse Logarithm \n "
                       "[4] Natural Logarithm  \n "
                       "[5] Inverse Natural Logarithm \n "
                       "[6] Switch Trig Units List \n "
                       "[7] Switch Trig Units Input \n "
                       "[8] Back \n")
    path.append(operation4)
    if operation4 == "1":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.factorial(a))
    elif operation4 == "2":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.log(a))
    elif operation4 == "3":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.ilog(a))
    elif operation4 == "4":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.nlog(a))
    elif operation4 == "5":
        a = main_app.getOneNumber()
        main_app.displayResult(calc.inlog(a))
    elif operation4 == "6":
        pass
    elif operation4 == "7":
        pass
    elif operation4 == "8":
        back(path)
    else:
        print("Enter a valid input.")

def back(path):
    # removes operation into this menu from path
    # returns to previous menu
    path.pop()
    path.pop()
    start_menu(path)


def run_menu():
    result = start_menu(path)
    return result

#run_menu(Cal)