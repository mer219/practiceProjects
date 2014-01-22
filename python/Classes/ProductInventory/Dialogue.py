class Dialogue:

    def promtMainMenu(self):
        print "Please select an action."
        print ""
        print "1. list products"
        print "2. add product"
        print "3. delete product"
        print "4. change product price"
        print "5. add product units"
        print "6. remove product units"

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

    def clear(self):
        os.system("clear")
