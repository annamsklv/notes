from functions import write_lines, get_lines, give_int
from constants import DATA_BASE, NOTE_TEMPLATE
import json
import csv


def export_to_rows():
    """
    Экспортирует контактные данные в файл формата csv
    в строку
    :return:
    """
    reader = get_lines()
    write_lines("rows.csv", reader)


def export_to_columns():
    """
    Экспортирует контактные данные в файл формата csv
    в столбик
    :return:
    """
    reader = get_lines()
    data = []
    for i in range(len(NOTE_TEMPLATE)):
        data.append(list(j[i] for j in reader))
    write_lines("columns.csv", data)


def export_to_json():
    """
    Экспортирует данные из БД в файл формата *.json
    :return:
    """
    with open(DATA_BASE, "r", newline='') as csvfile:
        reader = list(csv.DictReader(csvfile, dialect='excel', delimiter=";"))
    with open("lines.json", "w", newline='', encoding='windows1251') as file:
        file.write(json.dumps(reader, ensure_ascii=False, separators=(",", ":"), indent=4))


def output_menu():
    print("Выберите способ экспорта:")
    print("1. *.csv файл, в строку\n2. *.csv файл, в столбик\n3. *.json файл")
    input_choice = give_int('>> ', 1, 3)
    if input_choice == 1:
        export_to_rows()
    elif input_choice == 2:
        export_to_columns()
    elif input_choice == 3:
        export_to_json()
