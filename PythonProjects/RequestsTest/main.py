
import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                  "name": "generate",
                   "photo": "generate"
                   },
               headers={
                   'Content-Type': 'application/json', 
                  'trainer_token':'349c11c01fd49132546600dcc8d52596'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                   "pokemon_id": "28357",
                  "name": "Prode_Main",
                   "photo": "https://dolnikov.ru/pokemons/albums/.088png"
                    },
               headers={
                   'Content-Type': 'application/json', 
                   'trainer_token':'#YOUR_TOKEN'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json=
              {"pokemon_id": "28357"},
               headers={
                  'Content-Type': 'application/json', 
                   'trainer_token':'349c11c01fd49132546600dcc8d52596'
                       })
print(f'Code:{response.status_code} {response.reason}. Message:{response.text}')
