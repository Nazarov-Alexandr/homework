# С клавиатуры поступает строка. Необходимо вывести строку, где порядок слов в противоположном направлении.
# Первое слово с заглавной буквы, остальные с маленькой. Между словами только один пробел.
def F(x):
    s = x.split()
    y = []
    s.reverse()
    for a in s:
        y.append(a.lower())
    y[0] = y[0].capitalize()
    s = " ".join(y)
    return s


if __name__ == "__main__":
    print(F("пРивет мИР"))
    print(F("it    was    cool"))
    print(F("good"))