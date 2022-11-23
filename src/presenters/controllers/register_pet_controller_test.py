from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from .register_pet_controller import RegisterPetController
from src.presenters.helpers import HttpRequest, HttpResponse

faker = Faker()

def test_register_pet_handle():
    """Testing handler method calling register pet usecase"""
    
    register_pet_usecase = RegisterPetSpy(PetRepositorySpy(),UserRepositorySpy())
    register_pet = RegisterPetController(register_pet_usecase)
    
    attributes = {
        "name": faker.name(),
        "specie": faker.word(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name()
        }
    }
    
    response = register_pet.handle(
        http_request=HttpRequest(body=attributes)
    )
    
    # Testing inputs
    register_pet_usecase.register_params["name"] == attributes["name"]
    register_pet_usecase.register_params["specie"] == attributes["specie"]
    register_pet_usecase.register_params["age"] == attributes["age"]
    register_pet_usecase.register_params["user_information"] == attributes["user_information"]