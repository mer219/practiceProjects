class Collatz:

    def __init__(self):
        self.numberOfIterations = 0
        self.intermediaryResults = []

    def evaluateConjecture(self, numberToEvaluate):
        result = 0
        while int(numberToEvaluate) > 1:
            self.numberOfIterations += 1
            if self.numberIsOdd(numberToEvaluate):
                result = self.performOddProcessing(numberToEvaluate)
            else:
                result = self.performEvenProcessing(numberToEvaluate) 
            self.intermediaryResults.append(result)
            numberToEvaluate = result

    def numberIsOdd(self, inputNumber):
        remainder = int(inputNumber) % 2
        return remainder

    def performOddProcessing(self, inputNumber):
        result = 3*int(inputNumber)+1
        return result;

    def performEvenProcessing(self, inputNumber):
        result = int(inputNumber)/2
        return result

    def getNumberOfIterations(self):
        return self.numberOfIterations

    def printIntermediaryResults(self):
        outputString = ""
        stringCounter = 0
        for i in range(0, self.numberOfIterations):
            outputString = outputString + str(self.intermediaryResults[i]) + ", "
            stringCounter += 1
            if stringCounter == 10:
                print outputString
                outputString = ""
                stringCounter = 0
        if stringCounter > 0:
            print outputString
