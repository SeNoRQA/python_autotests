import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": "349c11c01fd49132546600dcc8d52596",
}

def test_get_trainers():
    """
    HW-1  GET /trainers
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 5}, timeout=5)
    assert response.status_code == 200, 'Unexpected status'

def test_get_trainer_by_id():
   """
   HW-2  GET /trainers by id
   """
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4719}, timeout=5)
   assert response.json()['trainer_name'] == 'Prod',""
   assert response.json()['city'] == 'Cheboksary', ""
   


def test_get_trainer_by_id2():
   """
   HW-3  GET /trainers by id
   """
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4719}, timeout=5)
   assert response.json()['city'] == 'Cheboksary', ""
   
def test_get_trainer_by_name():
   """
   HW-3  GET /trainers by name
   """
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4719}, timeout=5)
   assert response.json()['level'] == '1', ""
   assert response.json()['id'] == '4719', ""
   assert response.json()['city'] == 'Cheboksary', ""

   

