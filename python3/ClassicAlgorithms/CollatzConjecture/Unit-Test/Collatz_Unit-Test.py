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
        assert self.collatz.number_is_odd(3) == True

    def testNumberIsOddNegativeCase(self):
        assert self.collatz.number_is_odd(2) == False

    def testEvaluateConjectureOneCase(self):
        self.collatz.evaluate_conjecture(1)
        assert self.collatz.get_number_of_iterations() == 0

    def testEvaluateConjectureEightCase(self):
        self.collatz.evaluate_conjecture(8)
        assert self.collatz.getNumberOfIterations() == 3

    def testEvaluateConjectureEightCase(self):
        self.collatz.evaluate_conjecture(5)
        assert self.collatz.get_number_of_iterations() == 5

    def testgetNumberOfIterations(self):
        self.collatz.evaluate_conjecture(2)
        assert self.collatz.get_number_of_iterations() == 1

    def testPerformOddProcessing(self):
        result = self.collatz.perform_odd_processing(3)
        assert result == 10

    def testPerformEvenProcessing(self):
        result = self.collatz.perform_even_processing(4)
        assert result == 2

if __name__ == "__main__":
    unittest.main()
