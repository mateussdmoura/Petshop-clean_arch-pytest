from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repo import UserRepository
from src.infra.entities import Users as UsersModel

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
    
    engine.execute("DELETE FROM users WHERE id='{}';".format(new_user.id))
    
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password

def test_select_user():
    """Should select a user from Users table and compare it"""
    
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=user_id, name=name, password=password)
    
    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}', '{}', '{}');".format(
            user_id, name, password
        )
    )
    
    query_user1 = user_repo.select_user(user_id=user_id)
    query_user2 = user_repo.select_user(name=name)
    query_user3 = user_repo.select_user(user_id=user_id, name=name)
    
    assert data in query_user1
    assert data in query_user2
    assert data in query_user3
    
    engine.execute("DELETE FROM users WHERE id='{}';".format(user_id))