from faker import Faker
from .find import FindPet
from src.infra.test import PetRepositorySpy


faker = Faker()

def test_find_pet_by_id():
    
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)
    
    attributes = {
        "pet_id": faker.random_number(digits=5)
    }
    
    response = find_pet.by_id(attributes["pet_id"])
    
    # Testing input
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    
    # Testing output
    assert response["Success"] is True
    assert response["Data"]

def test_find_pet_by_id_fail():
    
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)
    
    attributes = {
        "pet_id": faker.word()
    }
    
    response = find_pet.by_id(attributes["pet_id"])
    
    # Testing input
    assert pet_repo.select_pet_params == {}
    
    # Testing output
    assert response["Success"] is False
    assert response["Data"] is None