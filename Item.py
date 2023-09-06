class Item():

    def __init__(self,description,price):
        self._description = description
        self._price = price

    def __str__(self):
        return f"Description: {self._description}\nPrice: ${self._price:,.2f}"

