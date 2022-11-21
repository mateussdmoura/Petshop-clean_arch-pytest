from faker import Faker
from .register import RegisterUserUseCase

faker = Faker()

def test_register_user_usecase():
    """Should be able to register new user to Users table"""
    
    name = faker.name()
    password = faker.word()
    
    sut = RegisterUserUseCase(
        name=name,
        password=password
    )
    