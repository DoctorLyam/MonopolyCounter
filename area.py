from base_class import Base
from user import User

class Area(Base):
    
    def init(self, name, price, rent, deposite_stock, dep_one_off, dep_two_off, 
            dep_three_off, dep_four_off, dep_industry, firm=False, office_count=0):
        self.name = name
        self.price = price
        self.rent = rent
        self.deposite = deposite_stock
        self.dep_one_off = dep_one_off
        self.dep_two_off = dep_two_off
        self.dep_three_off = dep_three_off
        self.dep_four_off = dep_four_off
        self.dep_industry = dep_industry
        self.firm = firm
        self.office_count = office_count

# Первая отрасль первой стороны
class First_1(Area):
    office_price = 50
    firm_price = 4*office_price + 50

harry_house = First_1(name='Дом Гарри', price=60, rent=2, deposite_stock=30, 
            dep_one_off=10, dep_two_off=30, dep_three_off=90, dep_four_off=160, dep_industry=250)
railway_st_kings_kross = First_1(name='Дом Гарри', price=60, rent=2, deposite=30, 
                        dep_one_off=20, dep_two_off=60, dep_three_off=180, dep_four_off=320, dep_industry=450)