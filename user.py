from base_class import Base
from area import Area

class User(Base):
    def init(self, name, areas, budget=200):
        self.name = name
        self.areas = areas
        self.budget = budget
    