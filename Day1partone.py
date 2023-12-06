temp_list = []
key = 0
count = 0
with open('information.txt') as lines_doc:
  for line in lines_doc.readlines():
    for char in line:
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
