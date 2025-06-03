# count é um Iterador sem fim(itertools)
from itertools import count

contador = count()
for i in contador:
    if i > 20:
        break
    print(i)