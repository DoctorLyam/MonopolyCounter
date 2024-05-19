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

# Транспортная отрасль
class Transport():
    def __init__(self, name, owner=''):
        self.name = name
        self.owner = owner

# Помощники
class Support():
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

class Second_1(Area):
    pass
class Second_1_son(Second_1):
    def __init__(self):
        self.name = 'Пинк'
        self.areas_list = ['Магазин Совы', 'Лавка Олливандера', 'Всё для Квиддича']
        self.areas_count = 3
        self.office_price = 50
        self.firm_price = 4*self.office_price + 50

class Second_2(Area):
    pass
class Second_2_son(Second_2):
    def __init__(self):
        self.name = 'Оранж'
        self.areas_list = ['Три метлы', 'Кабанья голова', 'Сладкое королевство']
        self.areas_count = 3
        self.office_price = 100
        self.firm_price = 4*self.office_price + 100

class Third_1(Area):
    pass
class Third_1_son(Third_1):
    def __init__(self):
        self.name = 'Ред'
        self.areas_list = ['Большой зал', 'Выручай Комната', 'Хижина Хагрида']
        self.areas_count = 3
        self.office_price = 150
        self.firm_price = 4*self.office_price + 150

class Third_2(Area):
    pass
class Third_2_son(Third_2):
    def __init__(self):
        self.name = 'Йелоу'
        self.areas_list = ['Карта Мародёров', 'Маховик времени', 'Меч Гриффиндора']
        self.areas_count = 3
        self.office_price = 150
        self.firm_price = 4*self.office_price + 150

class Fourth_1(Area):
    pass
class Fourth_1_son(Fourth_1):
    def __init__(self):
        self.name = 'Грин'
        self.areas_list = ['Бузинная палочка', 'Воскрешающий камень', 'Мантия-Невидимка']
        self.areas_count = 3
        self.office_price = 200
        self.firm_price = 4*self.office_price + 200

class Fourth_2(Area):
    pass
class Fourth_2_son(Fourth_2):
    def __init__(self):
        self.name = 'Пёпл'
        self.areas_list = ['Придира', 'Ежедневный пророк']
        self.areas_count = 2
        self.office_price = 200
        self.firm_price = 4*self.office_price + 200