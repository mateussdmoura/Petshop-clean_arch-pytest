from typing import Type, Dict, List
from src.domain.models import Users
from src.domain.test import mock_users
from src.data.repositories.users_repo_interface import UsersRepositoryInterface 

class FindUserSpy:
    """Class to define usecase: Select User"""
    
    def __init__(self, user_repo: Type[UsersRepositoryInterface]) -> None:
        self.user_repo = user_repo
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_param = {}
        
    def by_id(self, user_id: int) -> Dict[bool, Users]:
        self.by_id_param["user_id"] = user_id
        
        validate_entry = isinstance(id, int)
        
        if validate_entry:
            response = [mock_users()]
        
        return {
            "Success": validate_entry,
            "Data": response
        }
    
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        self.by_name_param["name"] = name
        
        validate_entry = isinstance(name, str)
        
        if validate_entry:
            response = [mock_users()]
        
        return {
            "Success": validate_entry,
            "Data": response
        }
    
    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        self.by_id_and_name_param["user_id"] = user_id
        self.by_id_and_name_param["name"] = name
        
        validate_entry = isinstance(user_id, int) and isinstance(name, str)
        
        if validate_entry:
            response = [mock_users()]
        
        return {
            "Success": validate_entry,
            "Data": response
        }
    