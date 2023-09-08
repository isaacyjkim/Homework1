# Represents an item a customer might buy at the store. It should have two attributes: a String for the item
# description and a double for the price. This class should also override the __str__ method in a nicely formatted way.
class Item():

    def __init__(self,description,price):
        self._description = description
        self._price = price

    def __str__(self):
        return f"Description: {self._description}\nPrice: ${self._price:,.2f}"

