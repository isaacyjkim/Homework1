from Item import Item
from Customer import Customer

def main():
    item1 = Item("apple",1.99)
    print(item1)
    customer1 = Customer("Isaac",True)
    customer2 = Customer("Bobby",True)


    customer1.purchase("Black tar heroin",100.00)
    customer2.purchase("Macbook",1000)
    print(customer1)
    print(customer2)




main()