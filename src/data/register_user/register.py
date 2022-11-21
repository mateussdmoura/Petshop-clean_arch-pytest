from typing import Type, Dict
from src.domain.use_cases import RegisterUserInterface
from src.data.repositories import UsersRepositoryInterface
from src.domain.models import Users

class RegisterUserUseCase(RegisterUserInterface):
    """Class to define Use Case Register User"""
    
    def __init__(self, users_repo: Type[UsersRepositoryInterface]):
        self.user_repo = users_repo
        
    def execute(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use-case
        
        Keyword arguments:
        name -- user's name
        password -- user's password
        Return: 
        """
        
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)
        
        if validate_entry:
            response = self.user_repo.insert_user(name, password)
            
        return {"Success": validate_entry, "Data": response}
        
    