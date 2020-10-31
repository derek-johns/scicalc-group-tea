#changing to main_app.py for import
import importlib
main_app = importlib.import_module("main-app")
import switch_mode

path = []

def start_menu(calc, path):
    operation = input("Perform a \n [1] Basic Functionality \n "
                      "[2] Simple Operations \n "
                      "[3] Scientific Operations \n "
                      "[4] Complex Operations \n [5] Exit \n")
    path.append(operation)
    if operation == "1":
        basics(calc, path)
    elif operation == "2":
        simple(calc, path)
    elif operation == "3":
        scientific(calc, path)
    elif operation == "4":
        complex(calc, path)
    elif operation == "5":
        pass
        #return "exit"
    else:
        print("Enter a valid input.")
        run_menu(calc)

def basics(calc, path):
    print("Basic Functionality")
    operation1 = input(" [1] Display value \n [2] Clear display \n "
                       "[3] Add value to memory \n [4] Clear memory \n "
                       "[5] Recall value in memory \n "
                       "[6] Switch display by input \n "
                       "[7] Back \n" )
    path.append(operation1)
    if operation1 == "1":
        pass
    elif operation1 == "2":
        pass
    elif operation1 == "3":
        calc.m_plus(main_app.m, main_app.m1)
    elif operation1 == "4":
        calc.m_reset(main_app.m, main_app.m1)
    elif operation1 == "5":
        calc.m_recall(main_app.m1)
    elif operation1 == "6":
        switch_mode.switch_display_input(main_app.mode)
        #print(main_app.mode)
    elif operation1 == "7":
        back(calc, path)
    else:
        print("Enter a valid input.")

def simple(calc, path):
    print("Simple Operations")
    operation2 = input(" [1] Add \n [2] Subtract \n [3] Multiply \n "
                       "[4] Divide \n [5] Square \n [6] Square Root \n "
                       "[7] Exponential \n [8] Inverse \n "
                       "[9] Change sign \n [10] Back \n")
    path.append(operation2)
    if operation2 == "1":
        a,b = main_app.getTwoNumbers()
        main_app.displayResult(calc.add(a,b))
        #return calc.add(a,b)
    elif operation2 == "2":
        pass
    elif operation2 == "3":
        pass
    elif operation2 == "4":
        pass
    elif operation2 == "5":
        pass
    elif operation2 == "6":
        pass
    elif operation2 == "7":
        pass
    elif operation2 == "8":
        pass
    elif operation2 == "9":
        pass
    elif operation2 == "10":
        back(calc, path)
    else:
        print("Enter a valid input." + "\n")

def scientific(calc, path):
    print("Scientific Operations")
    operation3 = input(" [1] Sine \n [2] Cosine \n [3] Tangent \n "
                       "[4] Inverse Sine \n [5] Inverse Cosine \n "
                       "[6] Inverse Tangent \n [7] Back \n")
    path.append(operation3)
    if operation3 == "1":
        pass
    elif operation3 == "2":
        pass
    elif operation3 == "3":
        pass
    elif operation3 == "4":
        pass
    elif operation3 == "5":
        pass
    elif operation3 == "6":
        pass
    elif operation3 == "7":
        back(calc, path)
    else:
        print("Enter a valid input.")

def complex(calc, path):
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
        pass
    elif operation4 == "2":
        pass
    elif operation4 == "3":
        pass
    elif operation4 == "4":
        pass
    elif operation4 == "5":
        pass
    elif operation4 == "6":
        pass
    elif operation4 == "7":
        pass
    elif operation4 == "8":
        back(calc, path)
    else:
        print("Enter a valid input.")

def back(calc, path):
    # removes operation into this menu from path
    # returns to previous menu
    path.pop()
    path.pop()
    start_menu(calc, path)


def run_menu(calc):

    start_menu(calc, path)

#run_menu(Cal)