from base_class import Base
from user import User

class Area(Base):
    name = None

class Muggle(Area):
    
    office_price = 50
    firm_price = 4*office_price + 50

    def init(self, name, rent, price, deposite, firm=False, office_count=0):
        self.name = name
        self.rent = rent
        self.price = price
        self.deposite = deposite
        self.firm = firm
        self.office_count = office_count

        