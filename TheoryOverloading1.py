# сравнение классов
class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    # сравнение
    def __eq__(self, others):
        return self.content == others.content

    # сложение
    def __add__(self, others):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        if isinstance(others, Backpack): # если others является классом Backpack
            new_obj.content.extend(others.content)
        else:
            new_obj.content.extend(others)

        return new_obj

    def __str__(self):
        return "Backpack: "+", ".join(self.content)


# сравнение
my_backpack = Backpack(gift="бутерброд")
son_backpack = Backpack(gift="банан")
if my_backpack == son_backpack:
    print("Как мы похожи")
if Backpack.__eq__(self=my_backpack, others=son_backpack):
    print("Как мы похожи")


# сложение
new_backpack = my_backpack + son_backpack+["сок"]
print(new_backpack)
