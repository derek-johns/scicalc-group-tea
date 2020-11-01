from calculator import Calculator
import sys
import menu
import switch_mode

m = [0]
m1 = [0]
display = 0
mode = "decimal"

def getOneNumber():
    a = float(input("number? "))
    return a

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    if type(x) == str:
        print(x, "\n")
    if type(x) == int or type(x) == float:
        x = round(x, 4)
        print(x, "\n")
        m.append(x)
    #print(m)
    #print(m1)
    return m


def performCalcLoop(calc):
    print("Welcome to the calculator")
    while True:
        result = menu.run_menu(calc)
        #print(result)
        #displayResult(result)
        if result == "exit":
            break

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
