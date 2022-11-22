from typing import Type, Dict, List
from src.domain.models import Users
from src.infra.repo import UserRepository
from src.domain.use_cases import FindUserInterface

class FindUser(FindUserInterface):
    """Class to define use case FindUser"""
    
    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repo = user_repository
        
    
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by id
        
        Keyword arguments:
        user_id -- id of user
        Return: Dict with success status and list with user
        """
        
        response = None
        validate_entry = isinstance(user_id, int)
        
        if validate_entry:
            response = self.user_repo.select_user(user_id=user_id)
        
        return {
            "Success": validate_entry,
            "Data": response
        }  
    
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User by name
        
        Keyword arguments:
        name -- user's name
        Return: Dict with success status and list with user
        """
        
        response = None
        validate_entry = isinstance(name, str)
        
        if validate_entry:
            response = self.user_repo.select_user(name=name)
        
        return {
            "Success": validate_entry,
            "Data": response
        }  
        
    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select User by id and name
        
        Keyword arguments:
        user_id -- user's id
        name -- user's name
        Return: Dict with success status and list with user
        """
        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)
        
        if validate_entry:
            response = self.user_repo.select_user(user_id=user_id, name=name)
        
        return {
            "Success": validate_entry,
            "Data": response
        }
        