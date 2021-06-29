# Реализуем модель человека
# Человеку можно есть, работать, играть, ходить в магазин
# У человека есть степень сытости, немного еды и денег
# Если сытость < 0, человек умирает
# Человеку надо прожить 365 дней
from random import randint
from termcolor import cprint
class Man:
    def __init__(self, name):
        self.fullness = 50
        self.food = 50
        self.money = 0
        self.name = name

    def __str__(self):
        return 'Я -{}, сытость: {}, еды осталось: {}, деньги: {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 10
            self.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        cprint('{} играл в Доту целый день'.format(self.name), color='yellow')
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            cprint('{} сходил  в магазин'.format(self.name), color='cyan')
            self.money -= 50
            self.food += 50
        else:
            cprint('{} : деньги кончились'.format(self.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint("{} умер".format(self.name), color='black')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
            return True
        elif self.food < 10:
            self.shopping()
            return True
        elif self.money < 50:
            self.work()
            return True
        elif dice == 1:
            self.work()
            return True
        elif dice == 2:
            self.eat()
            return True
        else:
            self.play_DOTA()
            return True


vasya = Man(name='Вася')
for day in range(1, 366):
    print('============={}========'.format(day))
    vasya.act()
    cprint(vasya, color='green')
    if vasya.act()  is None:
        break