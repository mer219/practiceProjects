import os

class Dialogue:

    def promptMainMenu(self):
        print "Please select an action."
        print ""
        print "1. list products"
        print "2. add product"
        print "3. delete product"
        print "4. change product price"
        print "5. add product units"
        print "6. remove product units"
        print "7. exit"

    def promptForProduct(self):
        print "Which product would you like to update?"

    def promptForNewPrice(self):
        print "What will the new price be?"

    def promptForQuantityRemoved(self):
        print "How many are being removed?"

    def promptForQuantityAdded(self):
        print "How many are being added?"

    def promptReturnToMainMenu(self):
        print "Press enter to return to the main menu"

    def promptNewProductName(self):
        print "Please enter the name of the new product"

    def promptNewProductQuantity(self):
        print "Please enter the quantity of the new product"

    def promptNewProductPrice(self):
        print "Please enter the price of the new product"

    def promptDeleteProductName(self):
        print "Please enter the name of the product you wish to remove"

    def promptNameOfProductForPriceChange(self):
        print "Please enter the name of the product you wish to change the price of"

    def promptForChagedPrice(self):
        print "Please enter the new price of the product"

    def promptAddUnitsProductName(self):
        print "Please enter the name of the product you will be adding units for"
    
    def promptNumberOfUnitsToAdd(self):
        print "How many units are being added"

    def promptRemoveUnitsProductName(self):
        print "Please enter the name of the product you will be removing units for"
    
    def promptNumberOfUnitsToRemove(self):
        print "How many units are being removed"
 
    def clear(self):
        os.system("clear")
