from CODES.oop.oop_fcc.items import Item


class Phone(Item):
    # all = []  # don't need, can use of parent

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

        # Phone.all.append(self)
