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
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))

        elif choice == 'mul':
            a, b = getTwoNumbers()
            displayResult(calc.mul(a, b))

        elif choice == 'div':
            a, b = getTwoNumbers()
            if b != 0:
                displayResult(calc.div(a, b))
            else:
                print("Can't divide /0")

        elif choice == 'sqr':
            a = float(input("Enter a number :"))
            displayResult(calc.sqr(a))

"""def exit():
    result = "exit"""""

        elif choice == 'sqroot':
            a = float(input("Enter a number :"))
            displayResult(calc.sqroot(a))

        elif choice == 'log':
            a = float(input("Enter a number :"))
            displayResult(calc.log(a))

        elif choice == 'ilog':
            a = float(input("Enter a number :"))
            displayResult(calc.ilog(a))

        elif choice == 'nlog':
            a = float(input("Enter a number :"))
            displayResult(calc.nlog(a))

        elif choice == 'inlog':
            a = float(input("Enter a number :"))
            displayResult(calc.inlog(a))

        elif choice == 'floor':
            a = float(input("Enter a number :"))
            displayResult(calc.floor(a))

        elif choice == 'ceil':
            a = float(input("Enter a number :"))
            displayResult(calc.ceil(a))

        else:
            print("That is not a valid input.")
# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
