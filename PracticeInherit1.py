# Реализуем модель доставки грузов
#
# Дорога - хранит расстояние между объектами
# Склад - хранит груз и управляет очередями грузовиков
# Базовый класс - Машина, имеет количество топлива, может заправляться,
#
# Грузовик - прпоизводный от машины
# Имеет емкость кузова, скорость движения, равход топлива за час поездки
# может стоять под погзуркой/разгрузкой
# ехать со скоростью
from termcolor import cprint


class Road:
    def __init__(self, start, end, distance):
        self.distance = distance
        self.end = end
        self.start = start


class Warehouse:

    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return "Склад: {}, груза: {}".format(self.name, self.content)

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print('{} прибыл грузовик {}'.format(self.name, truck))

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        print("{} прибыл грузовик {}".format(self.name, truck))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print("{} грузовик готов {} ".format(self.name, truck))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)

class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{}, топлива {}'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        return '{} заправился'.format(self.model)

class Truck(Vehicle):

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + 'груза {}'.format(self.cargo)

    def ride(self):
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print("{} Едет по дороге, осталось {}".format(self.model, self.distance_to_target))
        else:
            self.place = self.place.end
            self.place.truck_arrived(self)
            print("{} приехал".format(self.model))

    def go_to(self, road):
        self.place = road
        print("{} выехал в путь ".format(self.model))
        self.distance_to_target = road.distance
        print("{} выехал в путь".format(self.model))



    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif isinstance(self.place, Road):
            self.ride()


class AutoLoader(Vehicle):
    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        return 'грузим {}'.format(self.truck)

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
        elif self.truck is None:
            self.truck = self.warehouse.get_next_truck()
        elif self.role == 'loader':
            self.load()
        else:
            self.unload()

    def load(self):
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest

        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 1000000


moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

truck_1 = Truck(model='КАМАЗ', body_space=5000)
truck_2 = Truck(model='ГАЗ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0
while moscow.content > 0:
    hour += 1
    cprint("-----------------Час {}-------------------".format(hour), color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')






