from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import database
import view


def run(db_name, user='postgres', password='135798642', host='127.0.0.1', port=5433):
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(url)
    session = Session(bind=engine)
    database.drop_all_tables(engine)
    database.create_all_tables(engine)
    menu(session)


def menu(session):
    while True:
        view.show_main_menu_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            insert_menu(session)
        elif ch == 2:
            update_menu(session)
        elif ch == 3:
            delete_menu(session)
        elif ch == 4:
            select_menu(session)
        elif ch == 5:
            random_database(session, 20)
        elif ch == 6:
            show_record_with_word(session, input("Word: "))
        elif ch == 7:
            show_record_without_word(session, input("Word: "))
        elif ch == 8:
            show_records_in_interval(session, view.get_obj_for_search_in_interval())
        elif ch == 9:
            show_records_in_enum(session, view.get_enum())
        elif ch == 10:
            return
        else:
            print("Bad choice, try again...")


def insert_menu(session):
    while True:
        view.show_input_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.insert_into_train(session, view.get_obj_for_train())
        elif ch == 2:
            database.insert_into_carriage(session, view.get_obj_for_carriage())
        elif ch == 3:
            database.insert_into_seat(session, view.get_obj_for_seat())
        elif ch == 4:
            database.insert_into_station(session, view.get_obj_for_station())
        elif ch == 5:
            database.insert_into_ticket(session, view.get_obj_for_ticket())
        elif ch == 6:
            database.insert_into_type(session, view.get_obj_for_type())
        elif ch == 7:
            break
        else:
            print("Bad choice, try again...")


def delete_menu(session):
    while True:
        view.show_delete_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.delete_train(session, input("Input a number of train: "))
        elif ch == 2:
            database.delete_carriage(session, input("Input an id of carriage: "))
        elif ch == 3:
            database.delete_seat(session, input("Input an UID of seat: "))
        elif ch == 4:
            database.delete_station(session, input("Input a code of station: "))
        elif ch == 5:
            database.delete_ticket(session, input("Input ticket_id: "))
        elif ch == 6:
            database.delete_type(session, input("Input id: "))
        elif ch == 7:
            break
        else:
            print("Bad choice, try again...")


def update_menu(session):
    while True:
        view.show_update_buttons()
        ch = view.get_correct_number()
        if ch == 1:
            database.update_train_by_number(session, view.get_update_obj_for_train())
        elif ch == 2:
            database.update_carriage_by_number(session, view.get_obj_for_carriage())
        elif ch == 3:
            database.update_seat_by_id(session, view.get_update_obj_for_seat())
        elif ch == 4:
            database.update_station_by_code(session, view.get_update_obj_for_station())
        elif ch == 5:
            database.update_ticket_by_id(session, view.get_update_obj_for_ticket())
        elif ch == 6:
            database.update_type_by_id(session, view.get_update_obj_for_type())
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


def random_database(session, count):
    codes = []
    types = []
    trains = []
    carriages = []
    seats = []
    for code in range(1, count+1):
        database.insert_into_station(session, view.generate_random_name())
        codes.append(code)

    for type_id in range(1, int(count/4)):
        database.insert_into_type(session, view.generate_random_name())
        types.append(type_id)

    for train_number in range(1, count+1):
        database.insert_into_train(session, view.generate_random_train(codes))
        trains.append(train_number)

    for carriage_id in range(1, count+1):
        carriage = view.generate_random_carriage(trains, types)
        database.insert_into_carriage(session, carriage)
        carriages.append({"id": carriage_id, "seat_count": carriage["seat_count"]})

    for uid in range(1, count+1):
        database.insert_into_seat(session, view.generate_random_seat(carriages))
        seats.append(uid)

    for ticket_id in range(1, count+1):
        database.insert_into_ticket(session, view.generate_random_ticket(seats))


def show_record_with_word(session, word):
    response = database.full_text_ticket_search(session, word)
    view.print_response(response)
    return response


def show_record_without_word(session, word):
    response = database.full_text_seat_search(session, word)
    view.print_response(response)
    return response


def show_records_in_interval(session, obj):
    response = database.search_in_interval_train_carriage(session, obj)
    view.print_response(response)
    return response


def show_records_in_enum(cur, enum):
    response = database.search_in_enum(cur, enum)
    view.print_response(response)
    return response


if __name__ == "__main__":
    run('db_lab')
