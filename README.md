# Python.ScientificCalculator

## Description
* **Objective** - To implement an `ScientificCalculator` which displays output of basic and scientific computations.

## Git Collaboration
* Click the `fork` button in the top right corner to create a copy of this repository on your github account.

### Testing
* All tests passed.


### Core Features
* Following features:
  - A `state`, representing the value currently displayed on the calculator (default 0)
  - Get the current number on the display
  - Clear the display
  - Add, subtract, multiply, and divide the value on the `display` by a given number
  - Calculate the square (x<sup>2</sup>) and square root (√x) of the number on the display
  - Calculate variable exponentiation (x<sup>y</sup>)
  - Calculate the inverse of the number on the display (1/x)
  - Invert the sign of the number on the display (switch between positive and negative)
  - Update the display to `Err` if an error occurs (eg: Division by zero)
    - Errors cleared before any other operation can take place

* Each operation should automatically update the display

### Scientific Features
- Switch display mode (binary, octal, decimal, hexadecimal)
  - `switchDisplayMode()` should rotate through the options
  - `switchDisplayMode(String mode)` should set the display to the mode given
- Memory - Store up to one numeric value in memory for recall later (default to 0) *
  - (`M+` key) Add the currently displayed value to the value in memory (store in memory and update display) *
  - (`MC` key) Reset memory *
  - (`MRC` key) Recall the current value from memory to the display *
- Trig functions
  - Sine - Calculate the sine of the displayed value and display it
  - Cosine - Calculate the cosine of the displayed value and display it
  - Tangent - Calculate the tangent of the displayed value and display it
  - Inverse Sine
  - Inverse Cosine
  - Inverse Tangent
- Switch trig units mode (Degrees, Radians)
  - `switchUnitsMode()` should rotate through the options
  - `switchUnitsMode(String mode)` should set the trig units to the type given

### Bonus
- Factorial function  
- Logarithmic functions
  - Log
  - 10<sup>x</sup> (inverse logarithm)
  - Ln (natural logarithm)
  - e<sup>x</sup> (inverse natural logarithm)
