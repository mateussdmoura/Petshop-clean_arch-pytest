from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repo import UserRepository

faker = Faker()
user_repo = UserRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_user():
    """ Should insert user """

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()
    
    # SQL commands
    new_user = user_repo.insert_user(name=name,password=password)
    query_user = engine.execute("SELECT * FROM users WHERE id='{}';".format(new_user.id)).fetchone()
    
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password