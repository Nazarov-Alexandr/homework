# На вход подаётся 8-битное целое число со знаком (проверить нужно), на выходе вы должны вернуть перевёрнутое значение.
# Если значение выходит за пределы диапазона 8-битных целых чисел со знаком, тогда возвращаем сообщение ("no solution").
a = input()


def f(s1):
    res = ""
    n = int(s1)
    if n < 0:
        minus = -1
        s1 = s1[1:]
    else:
        minus = 1
    s2 = s1[::-1]
    s2 = int(s2)
    if s2 < -128 or s2 > 127:
        res = "no solution"
    else:
        res = s2*minus
    return res


print(f(a))
