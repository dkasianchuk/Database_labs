import psycopg2
from psycopg2.extras import DictCursor
from contextlib import closing
import database
import view
import string
import random


def run(db_name, user='postgres', password='135798642', host='127.0.0.1', port=5433):
    with closing(psycopg2.connect(dbname=db_name,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            database.drop_all_tables(cursor, conn)
            database.create_table_station(cursor, conn)
            database.create_table_type(cursor, conn)
            database.create_table_train(cursor, conn)
            database.create_table_carriage(cursor, conn)
            database.create_table_seat(cursor, conn)
            database.create_table_ticket(cursor, conn)
            menu(cursor, conn)


def menu(cur, conn):
    while True:
        view.show_main_menu_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            insert_menu(cur, conn)
        elif ch == 2:
            update_menu(cur, conn)
        elif ch == 3:
            delete_menu(cur, conn)
        elif ch == 4:
            select_menu(cur)
        elif ch == 5:
            pass
        elif ch == 6:
            return
        else:
            print("Bad choice, try again...")


def insert_menu(cur, conn):
    while True:
        view.show_input_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.insert_into_train(cur, conn, view.get_obj_for_train())
        elif ch == 2:
            database.insert_into_carriage(cur, conn, view.get_obj_for_carriage())
        elif ch == 3:
            database.insert_into_seat(cur, conn, view.get_obj_for_seat())
        elif ch == 4:
            database.insert_into_station(cur, conn, view.get_obj_for_station())
        elif ch == 5:
            database.insert_into_ticket(cur, conn, view.get_obj_for_ticket())
        elif ch == 6:
            database.insert_into_type(cur, conn, view.get_obj_for_type())
        elif ch == 7:
            break
        else:
            print("Bad choice, try again...")


def delete_menu(cur, conn):
    while True:
        view.show_delete_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.delete_train(cur, conn, input("Input a number of train: "))
        elif ch == 2:
            database.delete_carriage(cur, conn, input("Input an id of carriage: "))
        elif ch == 3:
            database.delete_seat(cur, conn, input("Input an UID of seat: "))
        elif ch == 4:
            database.delete_station(cur, conn, input("Input a code of station: "))
        elif ch == 5:
            database.delete_ticket(cur, conn, input("Input ticket_id: "))
        elif ch == 6:
            database.delete_type(cur, conn, input("Input id: "))
        elif ch == 7:
            break
        else:
            print("Bad choice, try again...")


def update_menu(cur, conn):
    while True:
        view.show_update_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.update_train_by_number(cur, conn, view.get_update_obj_for_train())
        elif ch == 2:
            database.update_carriage_by_number(cur, conn, view.get_obj_for_carriage())
        elif ch == 3:
            database.update_seat_by_id(cur, conn, view.get_update_obj_for_seat())
        elif ch == 4:
            database.update_station_by_code(cur, conn, view.get_obj_for_station())
        elif ch == 5:
            database.update_ticket_by_id(cur, conn, view.get_update_obj_for_ticket())
        elif ch == 6:
            database.update_type_by_id(cur, conn, view.get_obj_for_type())
        elif ch == 7:
            return
        else:
            print("Bad choice, try again...")


def select_menu(cur):
    while True:
        view.show_select_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            view.print_response(database.get_train_by_number(cur, input("Input a number of train: ")))
        elif ch == 2:
            view.print_response(database.get_carriage_by_id(cur, input("Input an id of carriage: ")))
        elif ch == 3:
            view.print_response(database.get_seat_by_uid(cur, input("Input an UID of seat: ")))
        elif ch == 4:
            view.print_response(database.get_station_by_code(cur, input("Input an id of station: ")))
        elif ch == 5:
            view.print_response(database.get_ticket_by_id(cur, input("Input id of ticket: ")))
        elif ch == 6:
            view.print_response(database.get_type_by_id(cur, input("Input id of type:")))
        elif ch == 7:
            return
        else:
            print("Bad choice, try again...")


def __generate_random_string(min_border, max_border):
    s = string.ascii_letters
    return ''.join(random.sample(s, random.randint(min_border, max_border)))


if __name__ == "__main__":
    run('db_lab')
