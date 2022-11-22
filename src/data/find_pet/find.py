from typing import Type, Dict, List
from src.domain.models import Users
from src.infra.repo import PetsRepository
from src.domain.use_cases import FindPetInterface

class FindPet(FindPetInterface):
    """Class to define use case FindUser"""
    
    def __init__(self, pet_repository: Type[PetsRepository]):
        self.pet_repo = pet_repository
        
    
    def by_id(self, pet_id: int) -> Dict[bool, List[Users]]:
        """Select User by id
        
        Keyword arguments:
        user_id -- id of user
        Return: Dict with success status and list with user
        """
        
        response = None
        validate_entry = isinstance(pet_id, int)
        
        if validate_entry:
            response = self.pet_repo.select_pet(pet_id=pet_id)
        
        return {
            "Success": validate_entry,
            "Data": response
        }  
    
    def by_user_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by name
        
        Keyword arguments:
        name -- user's name
        Return: Dict with success status and list with user
        """
        
        response = None
        validate_entry = isinstance(user_id, int)
        
        if validate_entry:
            response = self.pet_repo.select_pet(user_id=user_id)
        
        return {
            "Success": validate_entry,
            "Data": response
        }  
        
    def by_id_and_user_id(self, pet_id: int, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by id and name
        
        Keyword arguments:
        user_id -- user's id
        name -- user's name
        Return: Dict with success status and list with user
        """
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)
        
        if validate_entry:
            response = self.pet_repo.select_pet(pet_id=pet_id, user_id=user_id)
        
        return {
            "Success": validate_entry,
            "Data": response
        }
        