from api_call import create_final_pokemon
from calculate import calculate_winning_condition

def ending_stuff(poke_team):
  print("\nLet's see if you beat Mewtwo")
  input('\nPress Enter to continue')
  print("\nThis is your Pokemon:")
  pokemon_end_result = create_final_pokemon(poke_team)
  if pokemon_end_result:
    types, hp, special_attack, speed = pokemon_end_result
  print("\n TYPE/S: {} \n HP: {} \n SPECIAL-ATTACK: {}\n SPEED: {}".format(" ".join(types), hp, special_attack, speed))
  input("\nPress enter to see if you are a match for mewtwo:")
  calculate_winning_condition(types, hp, special_attack, speed)
