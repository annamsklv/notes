from constants import DATA_BASE
import csv
import os.path
from functions import write_lines
from constants import ABILITIES
import log

def fieldnames():
    """Create file.csv if it not exists, to avoid duplicate headers
    
    args -> None
    returns -> None
    """
    if not os.path.exists(
            DATA_BASE):  
        with open(DATA_BASE, 'a', newline='') as file:
            writer = csv.writer(file, dialect='excel', delimiter=';')
            writer.writerow(['Имя', 'Дата', 'Текст'])
            file.close()


def check_name(
        text):  
    """ Testing input data 

    args -> str (input text)
    retuns -> str
    """
    while not text.isalpha():
        text = input('Ошибка! Обязательное поле, повторите ввод: \n')
    return text.title()


def add_note():
    """ Adding data of new contact in csv-file. User inputs data (str), def create dict and add it in file.

    args -> None
    returns -> None
    """
    fieldnames()
    name = check_name(input('Введите название заметки: \n '))
    date = check_name(input('Введите дату: \n '))
    text = check_name(input('Введите текст заметки\n '))
    new_note = {'Название': name, 'Дата': date, 'Текст': text}

    log.add_logger(f"{ABILITIES[0]};{new_note}")

    with open(DATA_BASE, mode='a', newline='') as csv_file:
        field_names = ['Название', 'Дата', 'Текст']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(new_note)
        csv_file.close()
