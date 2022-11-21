from src.infra.config import DBConnectionHandler
from src.domain.models import Pets
from src.infra.entities import Pets as PetsModel


class PetsRepository:
    """ Class to manage Pets Repository """
    
    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Insert data in Petsentity entity 

        Args:
            name (str): name of the pet
            specie (str): Enum with species accepted
            age (int): pet's age
            user_id (int): id of the owner (FK)

        Returns:
            Pets: tuple with new pet inserted
        """
        
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name,specie=specie,age=age,user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()
                
                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value[0],
                    age=new_pet.age,
                    user_id=new_pet.user_id
                    )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        
        return None