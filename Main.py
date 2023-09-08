from Item import Item
from Customer import Customer

# Isaac Kim
# CIS 275 Advanced Python Programming
def main():

    item1 = Item("Apple",2.99)
    print(f"{item1}\n")

    customer1 = Customer("Isaac",False)
    customer2 = Customer("Bobby",True)


    customer1.purchase("Raw Honey",20.00)
    customer1.purchase("Ground beef 16 oz",10)

    customer2.purchase("Frozen pizza",10)
    customer2.purchase("Macbook",1000)
    print(customer1)
    print(customer2)




main()