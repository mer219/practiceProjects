#! /usr/bin/python

import Collatz

collatz = Collatz.Collatz()

print "Please enter a number to evaluate:"
number = raw_input("")
collatz.evaluateConjecture(number)
numberOfIterations = collatz.getNumberOfIterations()
print '{} evaluated to 1 after {} iterations'.format(number, numberOfIterations)
print 'the evaluated values for {} were:'.format(number)
collatz.printIntermediaryResults()
