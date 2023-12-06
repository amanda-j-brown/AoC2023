def points_for_card(card):
  end_of_card_num = card.index(":")
  winning_and_picked = card[end_of_card_num + 2:]

  separation = winning_and_picked.index("|")
  winning_num = winning_and_picked[:separation - 1]
  picked_num = winning_and_picked[separation + 2:]

  winning_num_list = winning_num.split(" ")
  picked_num_list = picked_num.split(" ")

  no_space_winning_num_list = winning_num_list
  while "" in no_space_winning_num_list:
    space = no_space_winning_num_list.index("")
    no_space_winning_num_list = no_space_winning_num_list[:space] + no_space_winning_num_list[space + 1:]


  no_space_picked_num_list = picked_num_list
  while "" in no_space_picked_num_list:
    space = no_space_picked_num_list.index("")
    no_space_picked_num_list = no_space_picked_num_list[:space] + no_space_picked_num_list[space + 1:]


  for i in range(len(no_space_winning_num_list)):
    no_space_winning_num_list[i] = int(no_space_winning_num_list[i])

  for i in range(len(no_space_picked_num_list)):
    no_space_picked_num_list[i] = int(no_space_picked_num_list[i])

  count = 0
  for num in no_space_winning_num_list:
    if num in no_space_picked_num_list:
      count += 1

  return 0 if count == 0 else 2 ** (count - 1)


with open('cards.txt') as lines_doc:
  total_points = 0
  for single_card in lines_doc.readlines():
    points = points_for_card(single_card)
    total_points += points

print(total_points)
