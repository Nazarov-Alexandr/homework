# Задаётся количество элементов в списке (>4). Задаётся целочисленный списокдлины N. Задаётся цель.
# Необходимо найти сумму 4 чисел, которые равны цели или находятся близко к ней и вывести их.
from math import inf
import itertools


def f(a, target):
    N = len(a)
    differ = inf
    comb = list(itertools.combinations(a, 4))
    index = ""
    for x in comb:
        summ = sum(x)
        s = abs(target-summ)
        if s < differ:
            differ = s
            index = x
    return index, sum(index)


if __name__ == "__main__":
    try:
        n = int(input("Задайте количество элементов в списке: "))
    except:
        print("пиши заново")
        exit(1)
    lst = []
    b = 1
    while b <= n:
        try:
            a = int(input(f"Элемент {b}: "))
        except ValueError:
            print("Введены некорректные данные. Повторите ввод")
            continue
        b = b + 1
            # exit(1)
        lst.append(a)
    print(lst)
    target = int(input("Введите цель: "))
    print(f(lst, target))