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

    def printProductList(self):
        for thisProductName in self.productList.keys():
            print '{}: #{} ${}'.format(self.productList[thisProductName].getId(), self.productList[thisProductName].getQuantityOnHand(), self.productList[thisProductName].getPrice())
