import sys

# def water_amount(input_str: str, water_flow: int = 1) -> str:
#     """
#     Docstring для water_amount
#         - Временная сложность О(N)

#     :param input_str: Входящая многострочная строка с данными в виде
#         1  строка: одно целое число N — количество доливов.
#         >1 строки: по два целых числа T_i и V_i, разделённые пробелом.
#     :type input_str: str
#     :param water_flow: Расход воды за единицу времени, по умолчанию равен 1
#     :type water_flow: int
#     :return: Возврат в виде строки c результатами расчётов
#     """
#     # Парсим строку и извлекаем необходимые нам данные
#     lines = input_str.strip().split('\n')
#     N = int(lines[0])
#     events_water = [map(int, lines[i].split())
#                         for i in range(1, N + 1)]

#     # Задаём начальные данные
#     current_water = 0
#     last_time = 0

#     for T_i, V_i in events_water:
#         # Расход воды за время t_i
#         # проверка не выхода в отрицательную зону
#         current_water -= (T_i - last_time) * water_flow
#         if current_water < 0:
#             current_water = 0
#         # Фиксируем в локальные переменные текущее время
#         # и оставшееся количество воды
#         current_water += V_i
#         last_time = T_i

#     return str(current_water)

# print(water_amount(sys.stdin.read()))

def maximize_num_into_str(A: str, B: str) -> str:
    """
    Docstring для maximize_num_into_str
        - Используется жадный алгоритм
        - Временная сложность O(m log m + n)

    :param A: Исходная числовая строка
    :type A: str
    :param B: Данные для преобразования
    :type B: str
    :return: Преобразованная строка
    :rtype: str
    """
    # Преобразуем строки в списки для удобства работы
    # причём В - сортируем по убыванию
    A_lst: list = list(A)
    B_lst: list = sorted(B, reverse=True)

    # указатель на текущую позицию в B
    b_index = 0
    for i in range(len(A_lst)):
        if b_index < len(B_lst) and B_lst[b_index] > A_lst[i]:
            # При выполнении условий, что цифра из В больше текущей из А
            # и мы не выходим за рамки строки В, производим замену
            A_lst[i] = B_lst[b_index]
            b_index += 1 # смещаем указатель вправо

    return ''.join(A_lst)

print(maximize_num_into_str(*sys.stdin.read().split(sep='\n')))