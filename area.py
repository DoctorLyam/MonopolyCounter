class Area():
    
    def __init__(self, name, price: int, deposite: int, rent_stock: int, rent_one_off: int, rent_two_off: int, 
            rent_three_off: int, rent_four_off: int, rent_firm: int, owner=''):
        self.name = name
        self.price = price
        self.deposite = deposite
        self.rent_stock = rent_stock
        self.rent_one_off = rent_one_off
        self.rent_two_off = rent_two_off
        self.rent_three_off = rent_three_off
        self.rent_four_off = rent_four_off
        self.rent_firm = rent_firm
        self.owner = owner

#Транаспортная отрасль
class Transport():
    def __init__(self, name, owner=''):
        self.name = name
        self.owner = owner

# Первая отрасль первой стороны
class First_1(Area):
    pass
class First_1_son(First_1):
    def __init__(self):
        self.name = 'Браун'
        self.areas_list = ['Дом Гарри', 'Вокзал Кингс-Кросс']
        self.areas_count = 2
        self.office_price = 50
        self.firm_price = 4*self.office_price + 50

# Вторая отрасль первой стороны
class First_2(Area):
    pass
class First_2_son(First_2):
    def __init__(self):
        self.name = 'Блю'
        self.areas_list = ['Отдел магического транспорта', 'Отдел тайн', 'Отдел обеспечения магического правопорядка']
        self.areas_count = 3
        self.office_price = 50
        self.firm_price = 4*self.office_price + 50