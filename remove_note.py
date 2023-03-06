from functions import get_lines, write_lines
from constants import DATA_BASE, NOTE_TEMPLATE
from search import search_by
from constants import ABILITIES
import log

def delete_note():
    reader = get_lines()
    choice = search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Couldn't find data"), log.add_logger(f"{ABILITIES[1]};{choice}; Couldn't find data")
    reader.insert(0, NOTE_TEMPLATE.keys())
    write_lines(DATA_BASE, reader)
    return print("Removing complete"), log.add_logger(f"{ABILITIES[1]};{choice}")
