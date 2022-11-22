from faker import Faker
from .register import RegisterUserUseCase
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_register_user_usecase():
    """Testin registry methods"""
    
    users_repo = UserRepositorySpy()
    register_user = RegisterUserUseCase(users_repo)
    
    attributes = {
        "name": faker.name(),
        "password": faker.word()
    }
    
    response = register_user.execute(
        name=attributes["name"],
        password=attributes["password"]
    )
    
    # Testing inputs
    assert users_repo.insert_user_params["name"] == attributes["name"]
    assert users_repo.insert_user_params["password"] == attributes["password"]
    
    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]

def test_register_user_usecase_fail():
    """Testin registry methods in fail"""
    
    users_repo = UserRepositorySpy()
    register_user = RegisterUserUseCase(users_repo)
    
    attributes = {
        "name": faker.random_number(digits=5),
        "password": faker.word()
    }
    
    response = register_user.execute(
        name=attributes["name"],
        password=attributes["password"]
    )
    
    # Testing inputs
    assert users_repo.insert_user_params == {}
    
    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
    