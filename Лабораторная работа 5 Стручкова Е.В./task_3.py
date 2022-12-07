from random import randint
def get_unique_list_numbers(start=-10, stop=10, count=15) -> list[int]:
    list_ = []
    while len(list_) < count:
        num_ = randint(start, stop)
        if num_ not in list_:
            list_.append(num_)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
