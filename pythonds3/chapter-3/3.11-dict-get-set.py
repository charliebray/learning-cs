import timeit
import random

for dict_size in range(1000, 101000, 1000):
    x = {j: random.randrange(dict_size) for j in range(dict_size)}
    random_index = random.randrange(dict_size)
    # Get item
    t_get = timeit.Timer(f'x[random_index]', 'from __main__ import random, x, random_index')
    get_time = t_get.timeit(number=1000)
    # Set Item
    t_set = timeit.Timer(f'x[random_index] = None', 'from __main__ import random, x, random_index')
    set_time = t_set.timeit(number=1000)
    print(f"{dict_size:<10,}{get_time:>10.6f}{set_time:>10.6f}")

