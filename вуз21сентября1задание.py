# С клавиатуры поступает строка. Необходимо вывести самую длинную подстроку без повторных символов.
def F(s):
    prom = ''
    result = ''
    for x in s:
        if x not in prom:
            prom = prom + x
        elif len(prom) > len(result):
            result = prom
            prom = x
    return result


if __name__ == '__main__':
    print(F('qweasdfdqw'))
    print(F('aaaaaaa'))
    print(F('prrker'))