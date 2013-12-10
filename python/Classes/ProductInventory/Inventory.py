class Inventory:
    product = dict()

    def addProduct(self, newProduct):
        productName = newProduct.getId()
        self.product[productName] = newProduct

    def removeProduct(self, productName):
        del self.product[productName]

    def printProductList(self):
        for thisProductName in self.product.keys():
            #print self.product[thisProductName].getId() + ": #" + self.product[thisProductName].getQuantityOnHand() + " $" + self.product[thisProductName].getPrice()
            print '{}: #{} ${}'.format(self.product[thisProductName].getId(), self.product[thisProductName].getQuantityOnHand(), self.product[thisProductName].getPrice())
