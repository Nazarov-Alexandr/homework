# Функция получает два списка. В каждом списке не должно быть дубликатов. Функция возвращает:
# 1) Количество элементов, присутствующих в обоих списках
# 2) Количество элементов, присутствующих только в одном списке
# 3) Количество оставшихся элементов в list1 после извлечения элементов из list2
# 4) Количество оставшихся элементов в list2 после извлечения элементов из list1
def f1(x, y):
    a = set(x)
    return a.intersection(y)


def f2(x, y):
    a = set(x)
    return a.symmetric_difference(y)


def f3(x, y):
    a = set(x)
    return a.difference(y)


def f4(x, y):
    a = set(y)
    return a.difference(x)


if __name__ == "__main__":
    list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
    list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    a1 = f1(list1, list2)
    a2 = f2(list1, list2)
    a3 = f3(list1, list2)
    a4 = f4(list1, list2)
    print(len(a1), "элемента:", *a1)
    print(len(a2), "элемента:", *a2)
    print(len(a3), "элемента:", *a3)
    print(len(a4), "элемента:", *a4)