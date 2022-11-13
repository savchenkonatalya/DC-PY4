from random import randint
def get_unique_list_numbers() -> list[int]:
    a = -10
    b = 10
    count = 15
    return set([randint(a, b) for i in range(count)])


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

