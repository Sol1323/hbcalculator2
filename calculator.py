"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_input = input(">>")
    # output = evaluate_input(user_input)
    # print(output)

    tokens = user_input.split(" ")
    operator = tokens[0].lower()

    if operator == "q":
        print("You have exited the calculator")
        break

    num1 = int(tokens[1])

    if len(tokens) < 3:
        num2 = 0
    elif len(tokens) == 3:
        num2 = int(tokens[2])

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "square":
        result = square(num1)
    elif operator == "cube":
        result = cube(num1)
    elif operator == "pow":
        result = power(num1, num2)
    elif operator == "mod":
        result = mod(num1, num2)

    print(result)
