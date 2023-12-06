def matching_games(game, red, green, blue):
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

  for num in blue_list:
    if num > blue:
      return False

  for num in red_list:
    if num > red:
      return False

  for num in green_list:
    if num > green:
      return False

  colon_pos = string_to_list[1].index(":")
  return int(string_to_list[1][:colon_pos])
  
possible_games = []
with open('games.txt') as lines_doc:
  for single_game in lines_doc.readlines():
    result = matching_games(single_game, 12, 13, 14)
    if result is False:
      continue
    else:
      possible_games.append(result)

print(possible_games)
print(sum(possible_games))
