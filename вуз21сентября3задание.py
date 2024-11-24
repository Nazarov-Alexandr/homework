# С клавиатуры поступает строка, которая имеет только символы: '(', ')', '{','}', '[' и ']'.
# Необходимо проверить правильно ли сформированы скобки. Если все скобки сформированы правильно,
# то вывести True, если нет, то вывести самую длинную правильно сформированную подстроку скобок,
# если такой подстроки нету, то вывести False.
# (Сначала лучше сделать True и False, а потом работать с подстроками).
def is_corrected(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif stack and stack[-1] == pairs[ch]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
def find_seq(s):
    max_length = 0
    current_length = 0
    max_seq = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subseq = s[i:j]
            if is_corrected(subseq):
                current_length = len(subseq)
                if current_length > max_length:
                    max_length = current_length
                    max_seq = subseq
    if max_seq == s:
        max_seq = True
    elif not max_seq:
        max_seq = False
    return max_seq


print(find_seq("(([()])()"))
