from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.infra.config import Base
import enum

class AnimalTypes(enum.Enum):
    """Defining animal types"""
    dog = 'dog',
    cat = 'cat',
    fish = 'fish',
    turtle = 'turtle'

class Pets(Base):
    """ Pets entity """
    
    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    specie = Column(Enum(AnimalTypes), nullable = False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    def __rep__(self):
        return f"Pet: [name={self.name}, species={self.specie}, user_id={self.user_id}"
    
    def __eq__(self, other):
        if (self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.user_id == other.user_id
            ):
            return True
        return False