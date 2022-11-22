from abc import ABC, abstractclassmethod
from typing import List, Dict
from src.domain.models import Pets

class FindPetInterface(ABC):
    """Interface to find user in db"""
    
    
    @abstractclassmethod
    def by_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Case"""
        
        raise Exception("Should implement method: by_id")

    @abstractclassmethod
    def by_user_id(cls, user_id: str) -> Dict[bool, List[Pets]]:
        """Case"""
        
        raise Exception("Should implement method: by_name")

    @abstractclassmethod  
    def by_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Case"""
        
        raise Exception("Should implement method: by_id_and_name")
    