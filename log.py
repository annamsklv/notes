from constants import DATA_BASE
from constants import LOG_NAME
from datetime import datetime as dt

"add, edit, remove"

LOGGER_TEMPLATE = {
    "Имя": "",
    "Фамилия": "",
    "Телефон": "",
    "Группа": "",
    "Комментарий": "",
    "Дата": "",
    "Операция": ""
}


def add_logger(data):
    """
    Writes information to the log. See the file name in constants or specify your own.
    :return:
    """
    datetime = dt.now().strftime('%Y-%m-%d, %H:%M:%S')
    with open('.\logger.log', 'a') as log_file:
        log_file.write('{}; {}\n'.format(datetime,data))
