from add_note import add_note
from user_interface import get_menu_item
from remove_note import delete_note
from edit_note import edit_note
from search import search_by
from show_db import show
import output


def procedure():
    while True:
        choice = get_menu_item()
        if choice == 1:
            add_note()
        elif choice == 2:
            delete_note()
        elif choice == 3:
            edit_note()
        elif choice == 4:
            search_by()
        elif choice == 5:
            show()
        elif choice == 6:
            output.output_menu()
        elif choice == 7:
            exit()
