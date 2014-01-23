import sys

#sys.path.append('/home/pi/src/practiceProjects/python/Classes/ProductInventory')
sys.path.append('..')

import unittest
import Inventory
import MockProduct

class InventoryTestClass(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory.Inventory()

    def tearDown(self):
        self.inventory = ""

    def testCreateProductSuccessCase(self):
        self.inventory.createProduct(MockProduct.MockProduct("createProductSuccessCase"))
        assert self.inventory.productExists("createProductSuccessCase") == True

    def testCreateProductFailureCase(self):
        self.inventory.createProduct(MockProduct.MockProduct("createProductFailureCase"))
        self.assertRaises(Exception, self.inventory.createProduct, MockProduct.MockProduct("createProductFailureCase"))

    def testProductExistsPositiveCase(self):
        self.inventory.createProduct(MockProduct.MockProduct("productExistsPositiveCase"))
        assert self.inventory.productExists("productExistsPositiveCase") == True

    def testProductExistsNegativeCase(self):
        assert self.inventory.productExists("productExistsNegativeCase") == False

    def testDeleteProductSuccessCase(self):
        self.inventory.createProduct(MockProduct.MockProduct("deleteProductSuccessCase"))
        self.inventory.deleteProduct("deleteProductSuccessCase")
        assert self.inventory.productExists("deleteProductSuccessCase") == False
         
    def testDeleteProductFailureCase(self):
        self.assertRaises(Exception, self.inventory.deleteProduct, "deleteProductFailureCase")

if __name__ == "__main__":
    unittest.main()
