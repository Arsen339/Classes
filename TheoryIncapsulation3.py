# Наследование
class Pet:

    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name


    def inspect(self):
        print(self.__class__.__name__, self.name) # сслыка на класс объекта и на имя класса
        print("Всего ног: ", 4)
        print("Хвост присутствует-", 'да' if self.has_tail else "нет")
        print(self.__dict__) # словарь катрибутов

class Cat(Pet):
    def sound(self):
        print("Мяу")

class Dog(Pet):
    def sound(self):
        print("Гав")


my_pet = Cat(name="Барсик")
my_pet.inspect()
my_pet.sound()


pet = Pet(name="кузя")
pet.inspect()
# Проверка, принадлежит ли объект классу
print(pet.__class__ is Pet)

class Bobtail(Cat):
    has_tail = False

my_pet1 = Bobtail(name="Бобтейл")
my_pet1.inspect()
my_pet1.sound()