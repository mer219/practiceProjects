class Collatz:
    numberOfIterations = 0
    intermediaryResults = []

    def evaluateConjecture(self, inputNumber):
        self.numberOfIterations += 1
        result = 0
        if self.numberIsOdd(inputNumber):
            result = self.performOddProcessing(inputNumber)
        else:
            result = self.performEvenProcessing(inputNumber) 
        self.intermediaryResults.append(result)
        if result > 1:
            self.evaluateConjecture(result)

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
