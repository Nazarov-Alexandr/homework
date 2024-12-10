# У вас есть лабиринт размером n x m, представленный в виде сетки. Вы начинаете в левом верхнем углу
# (ячейка [0][0]) и должны дойти до правого нижнего угла (ячейка [n-1][m-1]). Вы можете двигаться только
# вправо или вниз. Напишите рекурсивную функцию, которая возвращает количество возможных путей.
from functools import lru_cache


# @lru_cache() # встроенный инструмент кэширования
res = ["0", "1"]
def gen2(n):
    global res
    res2 = []
    for x in res:
        x1 = x + "0"
        x2 = x + "1"
        res2.append(x1)
        res2.append(x2)
    res = res2
    if len(res[0]) < n:
        gen2(n)

x = 4
y = 4
steps_x = x - 1
steps_y = y - 1
total_steps = steps_x + steps_y
gen2(total_steps)
res_final = []
for a in res:
    if steps_x == a.count("0"):
        res_final.append(a)
print(res_final, len(res_final))
print(res)
print(len(res_final))
