#!/usr/bin/env python3

# prompt the user input
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation(+, -, *, /): ")

# perform the calculation with matchcase

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by 0.")
        else:
            result = num1 / num2
            print (f"The result is {result}.")
    case _:
        print("Invalid operaton selected")
