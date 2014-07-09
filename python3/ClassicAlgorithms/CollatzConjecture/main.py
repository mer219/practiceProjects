#! /usr/bin/python3

import Collatz

collatz = Collatz.Collatz()

number = input("Please enter a number to evaluate\n")
collatz.evaluateConjecture(number)
numberOfIterations = collatz.getNumberOfIterations()
print(number, "evaluated to 1 after", numberOfIterations, "iterations")
print("the evaluated values for", number, "were")
collatz.printIntermediaryResults()
