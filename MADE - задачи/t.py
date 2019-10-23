n = int(input())
a = list(map(int, input().split()))

import itertools # подключение модуля

for i in itertools.permutations(a,len(a)):     # использование класса получения перестановок
    print (''.join(i))
