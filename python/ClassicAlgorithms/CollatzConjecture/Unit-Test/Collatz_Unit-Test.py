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

    def testgetNumberOfIterations(self):
        self.collatz.evaluateConjecture(2)
        assert self.collatz.getNumberOfIterations() == 1

    def testPerformOddProcessing(self):
        result = self.collatz.performOddProcessing(3)
        assert result == 10

    def testPerformEvenProcessing(self):
        result = self.collatz.performEvenProcessing(4)
        assert result == 2

if __name__ == "__main__":
    unittest.main()
