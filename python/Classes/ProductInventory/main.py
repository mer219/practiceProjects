#! /usr/bin/python

import Inventory
import Product

inventory = Inventory.Inventory()

inventory.addProduct(Product.Product(100, "tennis balls", 5))

inventory.printProductList()
