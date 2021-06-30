class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    # изменение объекта
    def __iadd__(self, others):
        self.content.extend(others.content)
        return self

    def __str__(self):
        return "Backpack: "+", ".join(self.content)

my_backpack = Backpack(gift="бутерброд")
son_backpack = Backpack(gift="банан")
my_backpack += son_backpack
print(my_backpack)