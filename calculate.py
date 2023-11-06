
def calculate_winning_condition(types, hp, special_attack, speed):
  points_to_win = 3
  points_of_mon = 0

  for type in types:
    if type == "bug" or type == "dark" or type == "ghost":
      points_of_mon += 1

  if hp > 105:
    points_of_mon +=1

  if special_attack > 130 :
    points_of_mon += 1

  if speed > 130 :
    points_of_mon += 1

  if points_of_mon == 0 or points_of_mon == 1:
    print("\n Mewtwo destroys you without problems")

  if points_of_mon == 2:
    print("\n Mewtwo is the winner, but doesn't leave the battle field unscathed")

  if points_of_mon >= 3:
    print("\n You beat Mewtwo and can call yourself a true Pokemon Champion!")




