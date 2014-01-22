import Dialog
import Product
import Invetory
import re

class Menu:
    dialogue = Dialogue.Dialogue()
    inventory = Inventory.Inventory()

    def __init__(self):
        self.mainMenuArray[1] = self.listProducts
        self.mainMenuArray[2] = self.addProduct
        self.mainMenuArray[3] = self.deleteProduct
        self.mainMenuArray[4] = self.changeProductPrice

    def startMenu(self):
        self.mainMenu()

    def mainMenu(self):
        dialogue.clear()
        dialogue.promptMainMenu()
        userInput = getMainMenuInput()
        self.mainMenuArray[userInput]

    def listProducts(self):
        dialogue.clear()
        inventory.printProductList()
        dialogue.promtReturnToMainMenu()
        userInput = raw_input("")
        self.mainMenu()

    def addProduct(self):
        dialogue.clear()
        dialogue.promptNewProductName()
        newProductName = raw_input("")
        dialogue.clear()
        dialogue.promptNewProductQuantity()
        newProductQuantity = raw_input("")
        dialogue.clear()
        dialogue.promptNewProductPrice()
        newProductPrice = raw_input("")
        inventory.createProduct(Product.Product(newProductQuantity, newProductName, newProductPrice))
        self.mainMenu()
      
    def deleteProduct(self):
        dialogue.clear()
        dialogue.promptDeleteProductName()
        productToBeDeleted = raw_input("")
        invetory.deleteProduct(productToBeDeleted)
        self.mainMenu()

    def changeProductPrice(self):
        dialogue.clear()
        dialogue.promptNameOfProductForPriceChange()
        productToChange = raw_input("")
        dialogue.promtForChangedPrice()
        newPrice = getNumericInput()

    def getMainMenuInput(self)
        userInput = raw_input("")
        if userInput > 0 and userInput <= 6:
            return userInput
        else:
            raise Exception("Invalid choice: exiting")

    def getNumericInput(self)
        userInput = raw_input("")
        numericRegex = re.compile('^[0-9]+$')
        regexResults = numericRegex.search(userInput)
        if regexResults != None:
            return userInput
        else:
            raise Exception("Invalid value: exiting")
