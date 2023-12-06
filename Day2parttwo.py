
def matching_games(game):
  string_to_list = game.split(" ")
  blue_list = []
  red_list = []
  green_list = []
  for i in range(len(string_to_list)):
    if string_to_list[i].startswith('blue'):
      blue_list.append(int(string_to_list[i-1]))
    elif string_to_list[i].startswith('green'):
      green_list.append(int(string_to_list[i-1]))
    elif string_to_list[i].startswith('red'):
      red_list.append(int(string_to_list[i-1]))

  return max(blue_list) * max(green_list) * max(red_list)


possible_games = []
with open('games.txt') as lines_doc:
  total_power = 0
  for single_game in lines_doc.readlines():
    result = matching_games(single_game)
    total_power += result

print(total_power)
