from constants import NOTE_TEMPLATE
from functions import give_int, get_lines


def search_by():
    """
    Ищет контакт, спрашивая поле, по которому искать и искомое значение.
    Возвращает все контакты, с совпашими значениями и предлагает выбрать один

    :return: список с контакнтыми данными для одного контакта
    """
    print(*NOTE_TEMPLATE.keys())
    print(f"\nВыберите один из артибутов по номеру, от 1 до {len(NOTE_TEMPLATE)}:")
    num = give_int(">> ", min_num=1, max_num=len(NOTE_TEMPLATE))
    atr = list(NOTE_TEMPLATE.keys())[num - 1]
    print(f"Выбран столбец '{atr}'")
    search_data = input("Введите искомое значение:\n>> ")
    reader = get_lines()
    data = []
    for row in reader:
        if search_data in row[num-1]:
            data.append(row)
    print(f"Найдено {len(data)} записей:")
    for i in data:
        print(*i)
    if len(data) > 1:
        print(f"\nВыберите одну из записей по номеру, от 1 до {len(data)}:")
        num = give_int(">> ", min_num=1, max_num=len(data))
        print(f"Выбрана запись {data[num - 1]}")
        return data[num - 1]
    else:
        return data
