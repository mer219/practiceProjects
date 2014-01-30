class Product:
    price = 0
    id = ""
    quantityOnHand = 0

    def __init__(self, id, price, initialQuantity):
        self.price = price
        self.id = id
        self.quantityOnHand = initialQuantity

    def setPrice(self, price):
        if price >= 0:
            self.price = price
        else:
            raise Exception("Price cannot be negative")

    def getPrice(self):
        return self.price

    def getId(self):
        return self.id

    def getQuantityOnHand(self):
        return self.quantityOnHand

    def addUnits(self, quantityAdded):
        self.quantityOnHand += quantityAdded

    def removeUnits(self, quantityRemoved):
        if quantityRemoved <= self.quantityOnHand:
            self.quantityOnHand -= quantityRemoved
        else:
            raise Exception("Quantity on hand cannot be negative")
