
import requests

URL = 'https://api.pokemonbattle.me:9104'
headers = {
    "Content-Type": "application/json",
    "trainer_token": "349c11c01fd49132546600dcc8d52596",
}


#body1 = {
#    "name": "Бартан",
#    "photo": "https://dolnikov.ru/pokemons/albums/045.png"
    
#}
#response = requests.post(url=f'{URL}/pokemons', json=body1, headers=headers, timeout=5)
#print(response)


#body2 = {
#    "pokemon_id": "28357",
#   "name": "ТЫнсТЫнс",
#    "photo": "https://dolnikov.ru/pokemons/albums/038.png"
#}



# requests.put(url=f'{URL}/pokemons', json=body2, headers=headers, timeout=5)
#print(response)


#body3 = {
#   "pokemon_id": "28357"
#}

# response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body3, headers=headers, timeout=5)
#print(response)
