# Функция получает список элементов. Любой элемент может встречаться более одного раза. Вернуть количество подмножеств,
# не содержащих повторяющихся элементов, не включая пустое множество. И сами подмножества.
import itertools


def f(list1):
    a = list(map(lambda x: set(itertools.combinations(list1, x)),  range(1, len(list1) + 1)))
    b = list(map(lambda x: set(x), itertools.chain.from_iterable(a)))
    return b


s = [1, 2, 3, 4]
# s = ["a", "b", "c", "d", "d"]
s = set(s)
x = f(s)
print("Подмножества:", *x)
print("Количество подмножеств:", len(x))