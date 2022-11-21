from faker import Faker
from .user_repo import UserRepository

faker = Faker()
user_repo = UserRepository()

def test_insert_user():
    """ Should insert user """

    name = faker.name()
    password = faker.word()
    
    new_user = user_repo.insert_user(name=name,password=password)
    
    print(new_user)