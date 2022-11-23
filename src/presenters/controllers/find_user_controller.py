from typing import Type
from src.domain.use_cases.find_user import FindUserInterface
from src.presenters.helpers import HttpRequest, HttpResponse


class FindUserController:
    """Class to define controller to find user usecase"""
    
    def __init__(self, find_user_usecase: Type[FindUserInterface]) -> None:
        self.find_user = find_user_usecase
    
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call usecase"""
        
        response = None
        
        if http_request.query:
            
            query_string_params = http_request.query.keys()
            
            if "user_id" in query_string_params and "user_name" in query_string_params:
                user_id = query_string_params["user_id"]
                user_name = query_string_params["user_name"]
                response = self.find_user.by_id_and_name(
                    user_id=user_id,
                    name=user_name
                )
            elif "user_id" in query_string_params and "user_name" not in query_string_params:
                user_id = query_string_params["user_id"]
                response = self.find_user.by_id(
                    user_id=user_id,
                )
            elif "user_id" not in query_string_params and "user_name" in query_string_params:
                user_name = query_string_params["user_name"]
                response = self.find_user.by_name(
                    name=user_name,
                )
            else:
                return {
                    "Success": False,
                    "Data": None
                }
            
            if response["Success"] is False:
                pass
        #return response