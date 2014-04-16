import sys

sys.path.append('..')

import unittest
import Collatz

class CollatzTestClass(unittest.TestCase):

    def setUp(self):
        self.collatz = Collatz.Collatz()

    def tearDown(self):
        self.collatz = ""

    def testNumberIsOddPositiveCase(self):
        assert self.collatz.numberIsOdd(3) == True

    def testNumberIsOddNegativeCase(self):
        assert self.collatz.numberIsOdd(2) == False

    def testEvaluateConjectureOneCase(self):
        self.collatz.evaluateConjecture(1)
        assert self.collatz.getNumberOfIterations() == 0

    def testEvaluateConjectureEightCase(self):
        self.collatz.evaluateConjecture(8)
        assert self.collatz.getNumberOfIterations() == 3

    def testEvaluateConjectureEightCase(self):
        self.collatz.evaluateConjecture(5)
        assert self.collatz.getNumberOfIterations() == 5

if __name__ == "__main__":
    unittest.main()
