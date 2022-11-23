from typing import Dict, Type, List
from src.domain.use_cases import RegisterPetInterface
from src.data.find_user import FindUser
from src.domain.models import Pets, Users
from src.data.repositories import PetsRepositoryInterface as PetsRepository
from src.infra.entities.pets import AnimalTypes

class PetRegister(RegisterPetInterface):
    """Class to define use case: Pet Register"""
    
    def __init__(self, pet_repo: Type[PetsRepository], find_user: Type[FindUser]) -> None:
        self.pet_repo = pet_repo
        self.find_user = find_user
        
    def execute(self, name: str, specie: str, user_information: Dict[int, str], age: int = None) -> Dict[bool, Pets]:
        """Register pet
        :params - name: pet's name
                - specie: Enum pet's specie
                - user_information: Dict with user_id and/or user_name
                - age: Pet's age, not mandatory
        :return - Dict with Success status and Pets data
        """
        
        response = None
        
        validate_entry = isinstance(name,str) and isinstance(specie, str)
        user = self.__find_user_info(user_information)
        checker = validate_entry and user["Success"]
        
        if checker:
            response = self.pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=user_information['user_id'])
        
        return {
            "Success": checker,
            "Data": response
        }
        
        
    def __find_user_info(self, user_information: Dict[int,str]) -> Dict[bool, List[Users]]:
        """Check user's info and select user
        :param  - user_information: Dict with user_id and/or user_name
        :return - Dict with response of find use case
        """
        
        user_found = None
        user_params = user_information.keys()
        
        if "user_id" in user_params and "user_name" in user_params:
            user_found = self.find_user.by_id_and_name(user_information['user_id'], user_information['user_name'])
        
        elif "user_id" not in user_params and "user_name" in user_params:
            user_found = self.find_user.name(user_information['user_name'])
        
        elif "user_id" in user_params and "user_name" not in user_params:
            user_found = self.find_user.name(user_information['user_id'])
        else:
            return {
                "Success": False,
                "Data": None
            }
        return user_found