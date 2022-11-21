from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets 

class PetsRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """"abstractmethod"""
        
        raise Exception("Method not implemented")
    