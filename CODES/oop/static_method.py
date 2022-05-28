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

    @staticmethod
    def is_integer(num):
        # we will remove floats that are point zero
        # eg 5.0, 2.0
        if isinstance(num, float):
            return num.is_integer()  # returns true if the float is integer that is 10.0 or something
        if isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


print(Item.is_integer(5.0))
