from base_class import Base
from area import Area

class User(Base):
    def __init__(self, name, areas=[], budget=2000):
        self.name = name
        self.areas = areas
        self.budget = budget

    def buy_area(self, area):
        if area not in self.areas and self.budget >= brown_one.price:
            self.areas.append(area)
            print(f'Игроку {self.name} добавлен участок {area.name}')
        elif area not in self.areas and self.budget < brown_one.price:
            print(f"Стоимость участка '{area.name}' слишком велика")
        elif area in self.areas:
            print(f'Участок уже принадлежит игроку {self.name}')

    def del_area(self, area):
        if area in self.areas:
            self.areas.append(area)
            print(f'Игроку {self} добавлен участок {area}')
        else:
            (f'Участка и так нет во владении')

user_1 = User(name="Саша")
user_2 = User(name="Настя")

brown_one = Area(name='Дом Гарри', price=6000, deposite=30, rent_stock=2, 
            rent_one_off=10, rent_two_off=30, rent_three_off=90, rent_four_off=160, rent_firm=250)
brown_two = Area(name='Вокзал Кингс-Кросс', price=60, deposite=30, rent_stock=4, 
            rent_one_off=20, rent_two_off=60, rent_three_off=180, rent_four_off=320, rent_firm=450)

user_1.buy_area(brown_one)