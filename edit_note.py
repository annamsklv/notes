from functions import get_lines, write_lines
from constants import DATA_BASE, NOTE_TEMPLATE
from search import search_by
from constants import ABILITIES
import log
from add_note import fieldnames, check_name
import csv
import os.path


def edit_note():
    reader = get_lines()
    choice = search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Couldn't find data"), log.add_logger(f"{ABILITIES[2]};{choice}; Couldn't find data")
    modify_key = input("""
Enter key number to modify field
Название        : [0]
Дата    : [1]
Текст   : [2]
""")
    edit_note = choice[0]
    name = edit_note[0]
    date = edit_note[1]
    text = edit_note[2]

    
    if modify_key == '0':
        name = check_name(input('Введите новое название: \n '))
    elif modify_key == '1':
        date = check_name(input('Введите новую дату: \n '))
    elif modify_key == '2':
        text = check_name(input('Введите новый текст:\n '))
    elif modify_key == '3':

        edit_note = {'Название': name, 'Дата': date, 'Текст': text}

    reader.insert(0, NOTE_TEMPLATE.keys())
    write_lines(DATA_BASE, reader)

    fieldnames()

    with open(DATA_BASE, mode='a', newline='') as csv_file:
        field_names = ['Название', 'Дата', 'Текст']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(edit_note)
        csv_file.close()

    return print("Edit complete"), log.add_logger(f"{ABILITIES[1]}; До редактирования:{choice}"), log.add_logger(f"{ABILITIES[2]}; Новая редакция: {edit_note}")
