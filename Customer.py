from Item import Item

class Customer():
    def __init__(self,name,status):
        self._name = name
        self._status = status
        self._item_list = []*5

    """""accepts a String and a double as parameters to represent the name and price of an item this customer is 
    purchasing. Create a new Item object with this info and append it to the internal list. If the customer is a 
    preferred customer based on the Boolean attribute's value, take 10% off the total sale price."""
    def purchase(self,name,price):
        if (self._status == True):
            price = price * .90
        item = Item(name,price)
        self._item_list.append(item)
    """Print the customer's name and every purchase that they have made. """
    def __str__(self):
        purchases = ""
        for i in self._item_list:
            purchases += f"{str(i)}\n"
        return f"\nCustomer name: {self._name}\nPurchases:\n{purchases}"

