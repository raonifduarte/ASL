import random

home = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4,
        5, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
away = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4]

print(random.choice(home), 'X', random.choice(away))
