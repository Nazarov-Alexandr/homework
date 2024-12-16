# У вас подарок, состоящий из 4-х конфет, и каждая конфета имеет свой цвет: red, green, blue, white, также
# у вас есть три одинаковых пакетадля распределения конфет. У вас получилось 6 комбинаций. Если будет 2 пакета
# вместо 3-х, то получится 7 комбинаций. Давайте рассмотрим ещё один пример: 2 пакета, но теперь 3 конфеты(RGB):
# У вас получилось 3 комбинации. Ваша задача создать функцию, котораю будет находить и возвращать количество даннных
# комбинаций. Данная функция принимает два целочисленных аргумента: Candies (количество конфет) и Packages (количество
# пакетов). Если Packages>Candies, то вернуть "No solution".
import random


def f(candies, packages):
    if packages > candies:
        return "No solution"
    elif packages == candies:
        return 1
    elif packages == 1:
        return 1
    result = set()
    candies_list = []
    for x in range(1, candies+1):
        candies_list.append(str(x))
    for y in range(packages-1):
        candies_list.append("_")
    print("candies list", candies_list)
    for n in range(1000):
        random.shuffle(candies_list)
        print(candies_list)
        buskets = []
        tmp = []
        for c in candies_list:
            if c != "_":
                tmp.append(c)
            else:
                if len(tmp) != 0:
                    buskets.append(tmp)
                    tmp = []
        if len(tmp) != 0:
            buskets.append(tmp)
        buskets = sorted(buskets)
        print(buskets, "buskets")
        if len(buskets) == packages:
            res = []
            for busket in buskets:
                busket = sorted(busket)
                res.append(",".join(busket))
            res.sort()
            tmp2 = "_".join(res)
            result.add(tmp2)
    print(result)
    return len(result)


print(f(5, 3))
