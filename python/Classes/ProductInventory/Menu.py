import Dialogue
import Product
import Inventory
import re

class Menu:
    dialogue = Dialogue.Dialogue()
    inventory = Inventory.Inventory()
    mainMenuArray = dict()

    def __init__(self):
        self.mainMenuArray[1] = self.listProducts
        self.mainMenuArray[2] = self.addProduct
        self.mainMenuArray[3] = self.deleteProduct
        self.mainMenuArray[4] = self.changeProductPrice
        self.mainMenuArray[5] = self.addProductUnits
        self.mainMenuArray[6] = self.removeProductUnits
        self.mainMenuArray[7] = self.endProgram

    def startMenu(self):
        self.mainMenu()

    def mainMenu(self):
        self.dialogue.clear()
        self.dialogue.promptMainMenu()
        userInput = self.getMainMenuInput()
        self.mainMenuArray[userInput]()

    def listProducts(self):
        self.dialogue.clear()
        self.inventory.printProductList()
        self.dialogue.promptReturnToMainMenu()
        userInput = raw_input("")
        self.mainMenu()

    def addProduct(self):
        self.dialogue.clear()
        self.dialogue.promptNewProductName()
        newProductName = raw_input("")
        self.dialogue.clear()
        self.dialogue.promptNewProductQuantity()
        newProductQuantity = self.getNumericInput()
        self.dialogue.clear()
        self.dialogue.promptNewProductPrice()
        newProductPrice = self.getNumericInput()
        self.inventory.createProduct(Product.Product(newProductName, newProductPrice, newProductQuantity))
        self.mainMenu()

    def addProductUnits(self):
        self.dialogue.clear()
        self.dialogue.promptAddUnitsProductName()
        productToUpdate = self.getProductNameInput()
        self.dialogue.promptNumberOfUnitsToAdd()
        numberOfAdditionalUnits = self.getNumericInput()
        self.inventory.increaseProductSupply(productToUpdate, numberOfAdditionalUnits)
        self.mainMenu()

    def removeProductUnits(self):
        self.dialogue.clear()
        self.dialogue.promptRemoveUnitsProductName()
        productToUpdate = self.getProductNameInput()
        self.dialogue.clear()
        self.dialogue.promptNumberOfUnitsToRemove()
        numberOfRemovedUnits = self.getNumericInput()
        self.inventory.decreaseProductSupply(productToUpdate, numberOfRemovedUnits)
        self.mainMenu()
      
    def deleteProduct(self):
        self.dialogue.clear()
        self.dialogue.promptDeleteProductName()
        productToBeDeleted = self.getProductNameInput()
        self.inventory.deleteProduct(productToBeDeleted)
        self.mainMenu()

    def changeProductPrice(self):
        self.dialogue.clear()
        self.dialogue.promptNameOfProductForPriceChange()
        productToChange = self.getProductNameInput()
        self.dialogue.clear()
        self.dialogue.promptForChangedPrice()
        newPrice = self.getNumericInput()
        self.inventory.changeProductPrice(productToChange, newPrice)
        self.mainMenu()

    def getMainMenuInput(self):
        userInput = raw_input("")
        userInput = int(userInput)
        if userInput > 0 and userInput <= len(self.mainMenuArray):
            return userInput
        else:
            raise Exception("Invalid choice: exiting")

    def getProductNameInput(self):
        userInput = raw_input("")
        if self.inventory.productExists(userInput) == True:
            return userInput
        else:
            raise Exception("Not a valid product")

    def getNumericInput(self):
        userInput = raw_input("")
        numericRegex = re.compile('^[0-9]+$')
        regexResults = numericRegex.search(userInput)
        if regexResults != None:
            userInput = int(userInput)
            return userInput
        else:
            raise Exception("Invalid value: exiting")

    def endProgram(self):
        self.dialogue.clear()
