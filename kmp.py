"""
Алгоритм Кнута-Морриса-Пратта

Строка для теста: abcabeabcabcabd
Подстрока: abcabd

Найденная позиция: 9
"""

text = input("Введите строку: ")
substring = input("Введите искомую подстроку: ")


def get_prefix_function(substring):
    # Префикс-функция (p[i] хранит максимальное кол-во символов, совпадающих с префиксом и заканчивающееся в позиции i)
    p = [0]
    i = 1  # Текущий индекс (конечный символ суффикса)
    j = 0  # Конечный индекс префикса
    while i != len(substring):
        if substring[i] == substring[j]:
            p.append(j + 1)
            i += 1
            j += 1
        else:
            if j == 0:
                p.append(0)
                i += 1
            else:
                j = p[
                    j - 1
                ]  # Возврат и поиск, начиная с другого (меньшего) подходящего префикса для той же позиции i
    return p


p = get_prefix_function(substring)
print(f"Префикс-функция: {p}")


def search(text, substring, p):
    i = 0  # Текущий индекс в строке
    j = 0  # Текущий символ искомой подстроки
    while i != len(text):
        if text[i] == substring[j]:
            i += 1
            j += 1
            if j == len(substring):
                return i - len(substring)
        else:
            if j != 0:
                j = p[j - 1]
            else:
                i += 1
    return -1


print(f"Результат поиска: {search(text, substring, p)}")