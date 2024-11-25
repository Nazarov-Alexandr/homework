# Задаётся список целых чисел.
# Вывести список разделённый списками со всеми возможными уникальными перестановками целых чисел из заданного списка.
import itertools
s = [1, 2, 3]
a = set(list(itertools.permutations(s)))
a = list(a)
for x in range(len(a)):
    a[x] = list(a[x])
print(a)