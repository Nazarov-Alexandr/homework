# Вы хотите ограбить банки вдоль улицы, которые идут подряд. В каждом банке есть сейф, в котором лежит
# определённая сумма денег (в миллионах рублей). Также в каждом банке есть система защиты, которая сработает, если
# были ограблены два ближайших банка. На вход поступает количество банков на улице. Далее пользователь вводит
# (по мере их расположения): название банка и сумму денег в сейфе.
# Вам необходимо вернуть максимальную сумму денег, которую вы можете получить (так, чтобы не сработала сигнализация),
# название банков и их порядковые номера на улице.
import itertools


def heist(s):
    indexes = list(map(lambda x: (x[0], x[1][1]), enumerate(s)))
    all_combinations = list(map(lambda x: set(itertools.combinations(indexes, x)),  range(1, len(indexes) + 1)))
    all_combinations = list(itertools.chain.from_iterable(all_combinations))

    def f1(x):
        s = []
        for a in range(0, len(x) - 1):
            if abs(x[a][0] - x[a + 1][0]) > 1:
                s.append(True)
            else:
                s.append(False)
        return all(s)

    acceptable_combinations = list(filter(f1, all_combinations))
    print(acceptable_combinations)

    def f2(x):
        s = 0
        for a in x:
            s = s + a[1]
        return s

    right_combinations = max(acceptable_combinations, key=f2)
    print(right_combinations)
    summa = f2(right_combinations)
    result = []
    result.append(summa)
    for x in range(0, len(right_combinations)):
        g = right_combinations[x][0]
        print(g)
        name = s[g][0]
        address = g + 1
        result.append((name, address))
    return result

if __name__ == "__main__":
    s = [("Sber", 10), ("Tin", 5), ("Vol", 6), ("Ker", 12)]
    # s = []
    # countt = int(input("Количество банков: "))
    # for x in range(countt):
    #     bank = input("Введите название банка и сумму через пробел: ")
    #     bank = bank.split()
    #     bank[1] = int(bank[1])
    #     s.append(tuple(bank))
    print(heist(s))
