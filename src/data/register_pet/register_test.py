from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from .register import PetRegister

faker = Faker()


def test_pet_registry():
    
    
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = PetRegister(pet_repo, find_user)
    
    attributes = {
        "name": faker.name(),
        "specie": 'dog',
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name()
        }
    }
    
    response = register_pet.execute(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"]
    )
    
    # Testing inputs
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]

    # Testing outputs
    assert find_user.by_id_and_name_param["user_id"] == attributes["user_information"]["user_id"]
    assert find_user.by_id_and_name_param["name"] == attributes["user_information"]["user_name"]

