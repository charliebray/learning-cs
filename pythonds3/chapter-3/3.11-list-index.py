import timeit
import random

for list_size in range(1000, 101000, 1000):
    random_index = random.randrange(list_size)
    x = list(range(list_size))
    t = timeit.Timer(f'x[random_index]', 'from __main__ import random, x, random_index')
    index_time = t.timeit(number=1000)
    print(f"{list_size:<10,}{index_time:>10.6f}, {random_index:>10,}")
