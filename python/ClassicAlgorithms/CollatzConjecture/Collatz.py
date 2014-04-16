class Collatz:

    def __init__(self):
        self.numberOfIterations = 0
        self.intermediaryResults = []
        #self.calculateMaxOddValue()

    def calculateMaxOddValue(self):
        self.maxOddValue = ~int(0)
        self.maxOddValue = self.maxOddValue >> 2
        if not self.numberIsOdd(self.maxOddValue):
            self.maxOddValue -= 1 
        print self.maxOddValue

    def evaluateConjecture(self, inputNumber):
        if int(inputNumber) > 1:
            self.numberOfIterations += 1
            result = 0
            if self.numberIsOdd(inputNumber):
                result = self.performOddProcessing(inputNumber)
            else:
                result = self.performEvenProcessing(inputNumber) 
            self.intermediaryResults.append(result)
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
