# На вход поступает строка и целое значение. Необходимо вывести строку в зигзагообразном виде,
# где целое значение обозначает количество строк. Другими типами данных пользоваться нельзя.
def f(s, n):
    a = [""]*n
    row = 0
    direction = 1
    for i in s:
        a[row] = a[row] + i
        if row < n - 1 and direction == 1:
            row = row + 1
        elif row > 0 and direction == -1:
            row = row - 1
        else:
            direction = direction*(-1)
            row = row + direction
    return "".join(a)


x = input()
tmp = x.split(",")
x = tmp[0]
y = int(tmp[1])
print(f(x, y))