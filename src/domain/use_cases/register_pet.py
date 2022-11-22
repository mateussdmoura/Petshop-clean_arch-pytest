from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Pets

class RegisterPetInterface(ABC):
    """Interface to RegisterUser use-case"""
    
    @abstractclassmethod
    def execute(cls, name: str, specie: str, user_information: Dict[int, str], age: int = None) -> Dict[bool, Pets]:
        """ Case """
        
        raise Exception("Should implement method: register")
        