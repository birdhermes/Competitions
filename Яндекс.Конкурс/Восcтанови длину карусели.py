import sys
from collections import Counter

l = [] # вводим массив
m = 0 # счетчик
numbers = sys.stdin.readline().strip() #Вводим числа
lin = input()
kin = sorted(lin)
c = Counter(lin)
for num in kin:
    if num not in l: l.append(num)
    else: m += 1 # добавление элемента в список
print(m)

print(c)