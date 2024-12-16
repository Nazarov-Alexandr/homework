# Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой ещё
# один список, который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс. Напишите функцию
# santa_users(), которая принимает двумерный список и возвращает словарь с элементом для каждого пользователя, где ключ-
# это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, то значение должно быть None.
user1 = ["John", 0]
user2 = ["Sam", 1]
user3 = ["Tom"]
users = [user1, user2, user3]


def santa_users(lists):
    a = dict()
    for user in lists:
        if len(user) == 2:
            a[user[0]] = user[1]
        if len(user) == 1:
            a[user[0]] = None
    return a


print(santa_users(users))