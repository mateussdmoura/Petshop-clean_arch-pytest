from typing import Dict, List, Type
from src.domain.models.pets import Pets
from src.domain.test import mock_pets, mock_users


class RegisterPetSpy:
    
    def __init__(self, pet_repo: any, find_user: any):
        self.pet_repo = pet_repo
        self.find_user = find_user
        self.register_params = {}
    
    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
        ) -> Dict[bool, Pets]:
        """Registry Pet"""
        
        self.register_params["name"] = name
        self.register_params["specie"] = specie
        self.register_params["user_information"] = user_information
        self.register_params["age"] = age
        
        
        response = None
        
        # Validating entry and trying to find an user
        
        validate_entry = isinstance(name,str) and isinstance(specie,str) and isinstance(user_information, dict)
        
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]
        
        if checker:
            response = mock_pets()
        
        return {
            "Success": checker, "Data": response 
        }
        
    def __find_user_info(self, user_information: Dict[int,str]) -> Dict[bool, List[Users]]:
        """Check user's info and select user"""
        
        user_found = None
        user_params = user_information.keys()
        
        if "user_id" in user_params and "user_name" in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        
        elif "user_id" not in user_params and "user_name" in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        
        elif "user_id" in user_params and "user_name" not in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        else:
            return {
                "Success": False,
                "Data": None
            }
        return user_found