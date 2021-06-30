# Создать модель жизни семьи
#
# Каждый день участники могут делать только одно действие
# Вместе они должны прожить год и не умереть
#
# Муж может:
# Есть
# Играть в WoT
# ходить на работу
# Жена может:
# Есть
# Покупать продукты
# Покупать шубу
# Убираться в доме
#
# Все они живут в доме
# Дом характеризуется
# Количеством денег в тумбочке(в начале = 100)
# Количеством еды в холодильнике(в начале - 50)
# кол-во грязи(в начале 0)
#
# У людей есть имя, степень сытости( в начале - 30), и степень счастья(в начале - 100)
#
# Любое действие, кроме "есть", уменьшает сытость на 10
# Кушает взрослый максимум по 30 единиц еды. Каждая единица еды = +1 к сытости
# Степень сытости не должна падать ниже 0, иначе человек умрет с голоду
# Деньги в тумбочку добавляет муж, после работы 100 единиц за раз
# Еда стоит 10 денег за 10 единиц. Шуба стоит 500 денег
#
# Грязь добавляется каждый день по 5 пунктов
# Если в доме грязи больше 30 единиц, степень счастья падает каждый день на 10 пунктов
# Степень счастья растет: у мужа от игры в WoT на 20, у жены от покупкишубы на 60
# Степень счастья не должны падать ниже 10, иначе человек умрет от депрессии
#
# Подвести итоги за год: сколько было съедено еды, заработано денег, куплено шуб
from termcolor import cprint
from random import randint

class House:
    def __init__(self, cash=100, food=50, dirt=0, cat_food=30):
        self.cash = cash
        self.food = food
        self.dirt = dirt
        self.cat_food = cat_food

    def __str__(self):
        return 'еды: {}, грязи: {}, денег {}, еды для кота {}'.format(self.food, self.dirt, self.cash, self.cat_food)

    def increase_dirt(self):
        self.dirt += 5

class Human:

    def __init__(self, happiness=100, fullness=30, name=None, home=None):
        self.name = name
        self.happiness = happiness
        self.fullness = fullness
        self.home = home

    def eat(self, amount):
        if self.home.food > amount:
            self.fullness += amount
            self.home.food -= amount
            print("{} поел/а".format(self.name))
        elif amount <= self.home.food:
            self.fullness += self.home.food
            self.home.food = 0
            print("{} поел/а".format(self.name))
        else:
            print("Нет еды")

    def go_to_house(self, house):
        self.home = house
        print("{} заехал/а в дом".format(self.name))

    def pet_the_cat(self):
        self.happiness += 5
        print("{} гладил кота".format(self.name))

    def suffer(self):
        if self.home.dirt >= 30:
            self.happiness -= 10
            print("Грязи больше 30 единиц, счастье уменьшается на 10 за день")

    def live_or_die(self):
        if self.fullness <= 0:
            print("{} dead of starving ".format(self.name))
            return None
        elif self.happiness < 10:
            print("{} dead of depression ".format(self.name))
            return None

        return True


class Cat:
    def __init__(self, name, fullness, home):
        self.name = name
        self.fullness = fullness
        self.home = home

    def __str__(self):
        return " Кот {} имеет степень сытости: {}".format(self.name, self.fullness)

    def eat(self, amount=10):
        self.fullness += amount * 2
        self.home.cat_food -= amount
        print("Кот {} поел".format(self.name))

    def sleep(self):
        self.fullness -= 10
        print("Кот {} спал".format(self.name))

    def tear_wallpaper(self):
        self.fullness -= 10
        print("Кот {} драл обои".format(self.name))

    def act(self):
        self.live_or_die()
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.tear_wallpaper()

    def live_or_die(self):
        if self.fullness <= 0:
            print("Cat {} dead of starving ".format(self.name))
            return None
        return True


class Husband(Human):

    def __init__(self, name, happiness, fullness, home):
        super().__init__(name=name, happiness=happiness, fullness=fullness, home=home)

    def __str__(self):
        return '{}, сытость: {}, стчатье: {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        self.suffer()
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat(amount=10)
        elif self.home.cash < 100:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat(amount=5)
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        self.home.cash += 100
        print('{} поработал'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        print('{} весь день играл в доту'.format(self.name))


class Wife(Human):
    def __init__(self, name, happiness, fullness, home):
        super().__init__(name=name, happiness=happiness, fullness=fullness, home=home)

    def __str__(self):
        return '{}, сытость: {}, стчатье: {}'.format(self.name, self.fullness, self.happiness)

    def shopping(self):
        if self.home.cash >= 30:
            self.home.cash -= 30
            self.home.food += 30
            self.fullness -= 10
            print("{} сходила в магазин за едой".format(self.name))
        elif 0 < self.home.cash < 30:
            self.home.cash -= self.home.food
            self.home.food = 0
            self.fullness -= 10
            print("{} сходила в магазин за едой".format(self.name))
        else:
            print("Нет денег на еду!")

    def buy_fur_coat(self):
        if self.home.cash >= 500:
            self.home.cash -= 500
            self.happiness += 60
            self.fullness -= 10
            print("{} купила шубу".format(self.name))
        else:
            print("Не хватает денег на шубу!")

    def clean_house(self):
        if self.home.dirt > 0:
            self.fullness -= 10
            self.home.dirt = 0
            print("{} отчистила дом от грязи".format(self.name))
        else:
            print("Дом и так чист!")

    def buy_kitecat(self):
        self.home.cat_food += 10
        self.home.cash -= 10
        print("{} купила еды коту".format(self.name))

    def act(self):
        self.suffer()
        dice = randint(1, 6)
        if self.home.dirt > 20 and self.fullness >= 30 and self.home.food >= 10:
            self.clean_house()
        elif self.home.cash > 600 and self.happiness < 20:
            self.buy_fur_coat()
        elif self.fullness < 30 and self.home.dirt <= 40 and self.home.food > 20:
            self.eat(amount=30)
        elif self.home.dirt > 30:
            self.clean_house()
        elif self.home.food < 30:
            self.shopping()
        elif self.home.cash > 550:
            self.buy_fur_coat()
        elif self.home.cat_food < 10:
            self.buy_kitecat()
        elif dice == 1:
            self.clean_house()
        elif dice == 2:
            self.eat(amount=30)
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.pet_the_cat()
        elif dice == 5:
            self.buy_kitecat()
        else:
            self.buy_fur_coat()


sweet_home = House()
vasya = Husband(name='Вася', happiness=100, fullness=30, home=None)
masha = Wife(name='Маша', happiness=100, fullness=30, home=None)
barsik = Cat("Барсик", 30, sweet_home)
vasya.go_to_house(sweet_home)
masha.go_to_house(sweet_home)

for day in range(365):

    cprint('=======================================День {} ===================='.format(day), color='red')
    masha.act()
    vasya.act()
    barsik.act()
    sweet_home.increase_dirt()
    cprint(vasya, color='blue')
    cprint(masha, color='red')
    cprint(barsik, color='cyan')
    cprint(sweet_home, color='cyan')
    if vasya.live_or_die() is None or masha.live_or_die() is None or barsik.live_or_die() is None:
        break
# edit
# Отцепить ветку develop и в ней начать добавлять котов в модель семьи
# Кот может: есть, спать, драть обои
# Люди могут гладить кота: растет счастье на 5 единиц
# В доме добавляется еда для кота: сначала 30 единиц
#
# У кота есть имя и степень сытости(в начале - 30)
# Любое действие, кроме "есть", уменьшает сытость на 10 пунктов
# Еда для кота: 10 денег за 10 единиц еды
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды
# Если сытость упадет ниже 0, кот умрет























