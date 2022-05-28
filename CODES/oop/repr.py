

class Item:
    pay_rate = 0.8
    store = []
    test = ["does", "it", "print", "this"]

    def __init__(self, name: str, price: float, quantity=0):
        # check
        assert price >= 0, f"price cannot be negative"
        assert quantity >= 0, f"quantity cannot be negative"

        # give value
        self.name = name
        self.price = price
        self.quantity = quantity

        # add to list when the object is instantiated
        Item.store.append(self)

    def total(self):
        return self.quantity * self.price

    def discount(self):
        return self.price * Item.pay_rate

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


item1 = Item("phone", 200, 2)
item2 = Item("laptop", 500, 5)
item3 = Item("mouse", 100, 3)
print(Item.store)
