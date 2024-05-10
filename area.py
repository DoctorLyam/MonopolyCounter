from base_class import Base

class Area(Base):
    
    def __init__(self, name, price, deposite, rent_stock, rent_one_off, rent_two_off, 
            rent_three_off, rent_four_off, rent_firm, firm=False, office_count=0):
        self.name = name
        self.price = price
        self.deposite = deposite
        self.rent_stock = rent_stock
        self.rent_one_off = rent_one_off
        self.rent_two_off = rent_two_off
        self.rent_three_off = rent_three_off
        self.rent_four_off = rent_four_off
        self.rent_firm = rent_firm
        self.firm = firm
        self.office_count = office_count


class Areas(Area):
    def __init__(self):
        self.areas_list = ['Дом Гарри', 'Вокзал Кингс-Кросс', 'Отдел магического транспорта', 'Отдел тайн', 'Отдел обеспечения магического правопорядка']


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



# blue_one = First_2(name='Отдел магического транспорта', price=100, deposite=50, rent_stock=6, 
#             rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
# blue_two = First_2(name='Отдел тайн', price=100, deposite=50, rent_stock=6, 
#             rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
# blue_three = First_2(name='Отдел обеспечения магического правопорядка', price=120, deposite=60, rent_stock=8, 
#             rent_one_off=40, rent_two_off=100, rent_three_off=300, rent_four_off=450, rent_firm=600)