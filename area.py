from base_class import Base
from user import User

class Area(Base):
    def init(self, name, price, industry, office_count, office_price, firm_price, firm = False):
        self.name = name
        self.price = price
        self.industry = industry
        self.office_count = office_count
        self.office_price = office_price
        self.firm_price = firm_price
        self.firm = firm