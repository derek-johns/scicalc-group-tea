from calculator import Calculator
import sys
import menu
import switch_mode

m = [0]
m1 = [0]
display = 0
mode = "decimal"

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")
    m.append(x)
    #print(m)
    #print(m1)
    return m


def performCalcLoop(calc):
    print("Welcome to the calculator")
    while True:
        menu.run_menu(calc)
        #print(result)
        #displayResult(result)
        #if result == "exit":
            #pass #user exits the calculator
        """choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        else:
            print("That is not a valid input.")"""

"""def exit():
    result = "exit"""""

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
