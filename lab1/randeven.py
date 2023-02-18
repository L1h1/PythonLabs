import random
def get_random_even_numbers():
    base_list=[random.randint(1,30) for i in range(30)]
    return [element for element in base_list if element%2==0]