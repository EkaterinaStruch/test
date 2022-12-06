from random import randint
def get_unique_list_numbers() -> list[int]:
    list_ = []
    start = -10
    stop = 10
    count = 15
    while len(list_) < count:
        num_ = randint(start, stop)
        if num_ not in list_:
            list_.append(num_)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
