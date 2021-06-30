class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class.__name__, self.model)

    def operate(self):
        print("Робот ездит по кругу")


class VacuumCleaningRobot(Robot):

    def __init__(self, model):
        # вызвать метод базового класса
        super().__init__(model=model)
        self.dust_bug = 0

    def operate(self):
        print("Робот пылесосит пол, запыленность мешка", self.dust_bug)


roomba = VacuumCleaningRobot(model='roomba M505')
print(roomba.model)
# Множественное наследование

class Employee:
    def salary(self):
        return 15000


class Parent:

    def childrens(self):
        return ["Вася", "Катя"]

class Man(Employee, Parent):
    pass


me = Man()
print(me.childrens())
print(me.salary())