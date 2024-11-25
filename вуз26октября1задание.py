# Задаётся список строк. Необходимо сгруппировать их в общий списокпо двум критериям:
# 1) слова имеют одни и те же буквы
# 2) слова одинаковой размерности
def f(x):
    res = {}
    for s in x:
        key = (len(s), frozenset(s))
        res.setdefault(key, [])
        res[key].append(s)
    return list(res.values())


if __name__ == "__main__":
    a = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
    print(f(a))
