# Динамическая типизация. Тип temperature не описан в конструкторе
class Robot():
    def __init__(self):
        self.name = "R2D2"

    def hello(self):
        print("Hello")


robot = Robot()
robot.temperature = 1
while robot.temperature < 10:
    robot.temperature = robot.temperature * 2
print(robot.temperature)
del robot.temperature
# динамическое переопределение
robot2 = Robot()
robot2.name = "Vally"
print(robot2.name)
# Проверка и установка атрибута
attr_name = "model"
if hasattr(robot, attr_name):
    print(robot.model)
else:
    setattr(robot, attr_name, 'android')
    print("attr set")
print(robot.model)
# удаление атрибута
delattr(robot, attr_name)
# проверка на пустой параметр
class Backpack:
    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print("В рюкзак положили", item)

    def inspect(self):
        print("В рюкзаке лежит")
        for item in self.content:
            print(' ', item)
    # удаление

    """def __del__(self):
        self.content = None
        print("Прощай мир")"""
    # переведем в стринг backpack.join-добавить

    def __str__(self):
        return "Backpack: " + ", ".join(self.content)

    def __len__(self):
        return len(self.content)


my_backpack = Backpack(gift = "флешка")
my_backpack.add(item="ноутбук")
my_backpack.add(item="зарядка для ноутбука")
my_backpack.inspect()
print(my_backpack)
print(len(my_backpack))

# аналогичные функции: __len__, __bool__
