import requests
import random

api_address = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0.'

def get_all_pokemon():
  response = requests.get(api_address)
  if response.status_code == 200:
    initial_response = response.json()['results']
    return initial_response
  else:
    return None

all_pokemon = get_all_pokemon()

def get_six_random_pokemon():
  random_pokemon = []
  for i in range(6):
    random_pokemon.append(random.choice(all_pokemon))
  return random_pokemon

random_pokemon = get_six_random_pokemon()

def create_final_pokemon(pokemon_list):
  pokemons = []
  types = []
  for pokemon in pokemon_list:
      response = requests.get(pokemon['url'])
      if response.status_code == 200:
        initial_response = response.json()
        pokemons.append(initial_response)
  types.append(pokemons[0]['types'][0]['type']['name'])
  if pokemons[0]['types'][1]['type']['name'] :
    types.append(pokemons[0]['types'][1]['type']['name'])
  hp = pokemons[1]['stats'][0]['base_stat']
  special_attack = pokemons[2]['stats'][3]['base_stat']
  speed = pokemons[3]['stats'][5]['base_stat']

  return types, hp, special_attack, speed




