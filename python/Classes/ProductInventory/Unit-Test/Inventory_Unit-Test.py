import sys

sys.path.append('..')

import unittest
import Inventory
import Product

class InventoryTestClass(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory.Inventory()

    def tearDown(self):
        self.inventory = ""

    def testProductExistsPositiveCase(self):
        self.inventory.createProduct(Product.Product("productExistsPositiveCase", 1, 1))
        assert self.inventory.productExists("productExistsPositiveCase") == True

    def testProductExistsNegativeCase(self):
        assert self.inventory.productExists("productExistsNegativeCase") == False

    def testCreateProductSuccessCase(self):
        self.inventory.createProduct(Product.Product("createProductSuccessCase", 1, 1))
        assert self.inventory.productExists("createProductSuccessCase") == True

    def testCreateProductFailureCase(self):
        self.inventory.createProduct(Product.Product("createProductFailureCase", 1, 1))
        self.assertRaises(Exception, self.inventory.createProduct, Product.Product("createProductFailureCase", 1, 1))

    def testDeleteProductSuccessCase(self):
        self.inventory.createProduct(Product.Product("deleteProductSuccessCase", 1, 1))
        self.inventory.deleteProduct("deleteProductSuccessCase")
        assert self.inventory.productExists("deleteProductSuccessCase") == False
         
    def testDeleteProductFailureCase(self):
        self.assertRaises(Exception, self.inventory.deleteProduct, "deleteProductFailureCase")

    def testIncreaseProductSupplySuccessCase(self):
        self.inventory.createProduct(Product.Product("increaseSupplySuccessCase", 1, 1))
        self.inventory.increaseProductSupply("increaseSupplySuccessCase", 1)
        assert self.inventory.productList["increaseSupplySuccessCase"].getQuantityOnHand() == 2

    def testIncreaseProductSupplyFailureCase(self):
        self.inventory.createProduct(Product.Product("increaseSupplyFailureCase", 1, 1))
        self.assertRaises(Exception, self.inventory.increaseProductSupply, "increaseSupplyFailureCase", 0)

    def testDecreaseProductSupplySuccessCase(self):
        self.inventory.createProduct(Product.Product("decreaseSupplySuccessCase", 1, 2))
        self.inventory.decreaseProductSupply("decreaseSupplySuccessCase", 1)
        assert self.inventory.productList["decreaseSupplySuccessCase"].getQuantityOnHand() == 1

    def testDecreaseProductSupplyFailureCaseDecreaseByZero(self):
        self.inventory.createProduct(Product.Product("decreaseSupplyByZeroFailureCase", 1, 1))
        self.assertRaises(Exception, self.inventory.decreaseProductSupply, "decreaseSupplyByZeroFailureCase", 0)
    
    def testDecreaseProductSupplyFailureCaseDecreaseToNegativeSupply(self):
        self.inventory.createProduct(Product.Product("decreaseSupplyToNegativeFailureCase", 1, 1))
        self.assertRaises(Exception, self.inventory.decreaseProductSupply, "decreaseSupplyToNegativeFailureCase", 2)

    def testSetPriceSuccessCase(self):
        self.inventory.createProduct(Product.Product("setPriceSuccessCase", 1, 1))
        self.inventory.changeProductPrice("setPriceSuccessCase", 2)
        assert self.inventory.productList["setPriceSuccessCase"].getPrice() == 2

    def testIncreaseProductSupplyFailureCase(self):
        self.inventory.createProduct(Product.Product("setPriceFailureCase", 1, 1))
        self.assertRaises(Exception, self.inventory.changeProductPrice, "setPriceFailureCase", -1)

if __name__ == "__main__":
    unittest.main()
