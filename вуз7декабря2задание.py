# Дано число n, представляющее количество пар скобок. Напишите функцию, которая генерирует все
# правильные скобочные последовательности длины 2n.
def gen(n, a):
    res = []
    if len(a[0]) < n:
        for x in a:
            x0 = x + "("
            x1 = x + ")"
            res.append(x0)
            res.append(x1)
        if len(res[0]) < n:
            return gen(n, res)
        else:
            return n, res
    else:
        return n, a


def check(s):
    while len(s.replace("()", "")) < len(s):
        s = s.replace("()", "")
    return len(s) == 0


def gen_sequences(n):
    strings = gen(2 * n, ["(", ")"])[1]
    res = []
    for x in strings:
        if check(x):
            res.append(x)
    return res


print(gen_sequences(5))