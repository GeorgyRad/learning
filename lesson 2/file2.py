"""Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

inner = input("Введите список через запятую \n")
list = inner.split(',')
idx = 0
while idx < len(list[:-1]):
    list[idx], list[idx+1] = list[idx+1], list[idx]
    idx += 2
print(list)