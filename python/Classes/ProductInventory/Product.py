class Product:
    price = 0
    id = ""
    quantityOnHand = 0

    def __init__(self, price, id, initialQuantity)
        self.price = price
        self.id = id
        self.quantityOnHand = initialQUantity

    def setPrice(self, price)
        self.price = price

    def getPrice(self)
        return self.price

    def setId(self, id)
        self.id = id

    def getId(self)
        return self.id

    def getQuantityOnHand(self)
        return self.quantityOnHand

    def addUnits(self, quantityAdded)
        self.quantityOnHand += quantityAdded

    def removeUnits(self, quantityRemoved)
        self.quantityOnHand -= quantityRemoved
