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

# Первая отрасль первой стороны
class First_1(Area):
    office_price = 50
    firm_price = 4*office_price + 50

brown_one = First_1(name='Дом Гарри', price=60, deposite=30, rent_stock=2, 
            rent_one_off=10, rent_two_off=30, rent_three_off=90, rent_four_off=160, rent_firm=250)
brown_two = First_1(name='Вокзал Кингс-Кросс', price=60, deposite=30, rent_stock=4, 
            rent_one_off=20, rent_two_off=60, rent_three_off=180, rent_four_off=320, rent_firm=450)

# Вторая отрасль первой стороны
class First_2(Area):
    office_price = 50
    firm_price = 4*office_price + 50

blue_one = First_2(name='Отдел магического транспорта', price=100, deposite=50, rent_stock=6, 
            rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
blue_two = First_2(name='Отдел тайн', price=100, deposite=50, rent_stock=6, 
            rent_one_off=30, rent_two_off=90, rent_three_off=270, rent_four_off=400, rent_firm=550)
blue_three = First_2(name='Отдел обеспечения магического правопорядка', price=120, deposite=60, rent_stock=8, 
            rent_one_off=40, rent_two_off=100, rent_three_off=300, rent_four_off=450, rent_firm=600)