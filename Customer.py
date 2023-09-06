from Item import Item

class Customer():
    def __init__(self,name,status):
        self._name = name
        self._status = status
        self._item_list = []*5

    def purchase(self,name,price):
        if (self._status == True):
            price = price * .90
        item = Item(name,price)
        self._item_list.append(item)

    def __str__(self):
        purchases = ""
        for i in self._item_list:
            purchases += str(i)
        return f"Name: {self._name}\nPurchases:\n{purchases}"

