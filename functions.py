from typing import Optional
from typing import List
from constants import DATA_BASE
import csv


def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')


def get_list_data(filename: str) -> List[str]:
    '''
    Возвращает список из строк файла
    Args:
    filename - имя файла
    Returns:
    List[str]
    '''
    with open(filename) as file:
        return file.read().split('\n')


def get_lines():
    """
    Считывает строки из базы данных и возвращает список,
    каждый элемент которого соответствует контакту

    :return:
    """
    with open(DATA_BASE, "r", newline='') as csvfile:
        result = csv.DictReader(csvfile, dialect='excel', delimiter=";")
        data = []
        for row in result:
            data.append(list(row.values()))
    return data


def write_lines(file_name: str, data):
    """
    Записывает данные в csv файл, разбивая список по колонкам
    :param file_name: имя выходного файла
    :param data: входящий список данных

    :return:
    """
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=';')
        for i in data:
            writer.writerow(i)
