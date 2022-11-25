list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[0]
for index, current_number in enumerate(list_numbers):
    max_number = list_numbers[max_index]
    if current_number >= max_number:
        max_index = index
        max_number = current_number

last_index = 0
last_number = list_numbers[0]
for index_1, number_1 in enumerate(list_numbers):
    last_number = list_numbers[last_index]
    if index_1 > last_index:
        last_index = index_1
        last_number = number_1

list_numbers[max_index] = last_number
list_numbers[last_index] = max_number
print(list_numbers)
