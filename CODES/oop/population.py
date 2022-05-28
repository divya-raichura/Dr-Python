class Human:
    pop = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.pop += 1

    @staticmethod
    def fun(self):
        # Human.pop = 0
        print('this is ' + self.name)

    @classmethod
    def atom_bomb(cls):
        cls.pop = 0

    def __repr__(self):  # tostring method like in Java
        return self.name


kunal = Human("Kunal", 18)
elon = Human("Elon", 50)
# print(kunal.fun(elon))
# print(Human.pop)
# print(elon.pop)
# print(kunal.pop)
# Human.atom_bomb()
#
# print(Human.pop)
# print(elon.pop)
# print(kunal.pop)
print(kunal)
