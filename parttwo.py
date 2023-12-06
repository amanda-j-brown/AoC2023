temp_list = []
key = 0
number_dict = {'one': 1,
              'two': 2,
              'tw': 2,
              'three': 3, 
              'four': 4, 
              'five': 5, 
              'six': 6, 
              'seven': 7, 
              'eight': 8,
              'eigh': 8,
              'igh': 8, 
              'ight': 8,
              'nine': 9, 
              'nin': 9}

def find_numbers(num, given_string):
  if num in given_string:
    num_word_len = len(num)
    replace = str(number_dict[num])
    start_num_pos = given_string.index(num)
    end_num_pos = start_num_pos + num_word_len
    if end_num_pos < len(given_string):
      return given_string[:start_num_pos] + replace + given_string[end_num_pos:]
    else:
      return given_string[:start_num_pos] + replace

with open('information.txt') as lines_doc:
  for line in lines_doc.readlines():
    new_string = line
    for num in number_dict:
      count_num_repeats = new_string.count(num)
      if count_num_repeats > 0:
        for i in range(count_num_repeats):
          new_string = find_numbers(num, new_string)

    for char in new_string:
      if char.isdigit():
        temp_list.append(char)

    if len(temp_list) == 1:
      temp_list = temp_list + temp_list
    else:
      temp_list = [temp_list[0]] + [temp_list[-1]]

    temp_list_sum = 0
    temp_list_sum = int(temp_list[0]) * 10 + int(temp_list[1])

    key += temp_list_sum

    temp_list = []

print(key)
