class Inventory:
    productList = dict()

    def productExists(self, productName):
        if productName in self.productList:
            return True
        else:
            return False

    def createProduct(self, newProduct):
        productName = newProduct.getId()
        if not self.productExists(productName):
            self.productList[productName] = newProduct
        else:
            raise Exception("Unable to add product.  Product already exists")

    def deleteProduct(self, productName):
       if self.productExists(productName):
            del self.productList[productName]
       else:
            raise Exception("Unable to delete product.  Product not in inventory") 

    def increaseProductSupply(self, productName, quantityIncreased):
       if quantityIncreased > 0:
           self.productList[productName].addUnits(quantityIncreased)
       else:
           raise Exception("Supply must increase by at least 1")

    def decreaseProductSupply(self, productName, quantityDecreased):
       if quantityDecreased > 0:
           self.productList[productName].removeUnits(quantityDecreased)
       else:
           raise Exception("Supply must decrease by at least 1")

    def changeProductPrice(self, productName, newPrice):
       self.productList[productName].setPrice(newPrice)

    def printProductList(self):
        for thisProductName in self.productList.keys():
            print '{}: #{} ${}'.format(self.productList[thisProductName].getId(), self.productList[thisProductName].getQuantityOnHand(), self.productList[thisProductName].getPrice())
