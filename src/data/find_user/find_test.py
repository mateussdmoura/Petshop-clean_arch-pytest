from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_find_by_id():
    """Testing find by id method"""
    
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)
    
    attributes = {
        "id": faker.random_number(digits=5)
    }
    
    response = find_user.by_id(user_id=attributes["id"])
    
    # Testing inputs
    assert user_repo.select_user_params["user_id"] == attributes["id"]
    
    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]
    
def test_find_by_id_fail():
    """Testing find by id method to fail"""
    
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)
    
    attributes = {
        "id": faker.word()
    }
    
    response = find_user.by_id(user_id=attributes["id"])
    
    # Testing inputs
    assert user_repo.select_user_params == {}
    
    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None