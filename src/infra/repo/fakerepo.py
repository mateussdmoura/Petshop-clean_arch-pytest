from src.infra.config import DBConnectionHandler
from src.infra.entities import Users

class FakeRepo:
    """ A simple repo """
    
    @classmethod
    def insert_user(cls):
        """ something """
        
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name='Mateus', password='Simas')
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()