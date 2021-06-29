# Создать двух людей, живущих в одном доме: Бивеса и Баттхеда
# Нужен класс дом, в нем должен быть холодильник с едой и тумбчка с деньгами
# Еда пусть хранится в хрлодильнике, в доме, а деньги в тумбочке
from random import randint
from termcolor import cprint
class Man:
    def __init__(self, name):
        self.fullness = 50
        self.name = name
        self.house = None

    def __str__(self):
        return 'Я -{}, сытость: {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='yellow')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил  в магазин'.format(self.name), color='cyan')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} : деньги кончились'.format(self.name), color='red')

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} заехал в дом'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint("{} умер".format(self.name), color='black')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
            return True
        elif self.house.food < 10:
            self.shopping()
            return True
        elif self.house.money < 50:
            self.work()
            return True
        elif dice == 1:
            self.work()
            return True
        elif dice == 2:
            self.eat()
            return True
        else:
            self.watch_MTV()
            return True

class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'Денег осталось: {},  еды осталось: {}'.format(self.food, self.money)


citizens = [
    Man(name='Бивис'),
    Man(name='Баттхед'),
    Man(name='Кенни')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)


for day in range(1, 366):
    print('============={}========'.format(day))
    for citizen in citizens:
        citizen.act()
    for citizen in citizens:
        cprint(citizen, color='green')
    cprint(my_sweet_home, color='green')
    for citizen in citizens:
        if citizen.act() is None:
            break