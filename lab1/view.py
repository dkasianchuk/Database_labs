def show_main_menu_buttons():
    print("1.Add new record.")
    print("2.Update an existing record.")
    print("3.Delete record.")
    print("4.Show record.")
    print("5.Random database.")
    print("6.Exit.")


def show_input_buttons():
    print("1.Add a new train.")
    print("2.Add a new carriage.")
    print("3.Add a new seat.")
    print("4.Add a new station")
    print("5.Add a new ticket.")
    print("6.Add a new type of carriage.")
    print("7.Go back.")


def show_delete_buttons():
    print("1.Delete train by number.")
    print("2.Delete carriage by id.")
    print("3.Delete seat by UID.")
    print("4.Delete station by code.")
    print("5.Delete ticket by id.")
    print("6.Delete type by id.")
    print("7.Go back.")


def show_update_buttons():
    print("1.Update a train by number of train.")
    print("2.Update a carriage by number of carriage.")
    print("3.Update a seat by UID.")
    print("4.Update a station by code.")
    print("5.Update a ticket by id.")
    print("6.Update a type by id.")
    print("7.Go back.")


def show_select_buttons():
    print("1.Get train by number of train.")
    print("2.Get carriage by number of carriage.")
    print("3.Get seat by UID.")
    print("4.Get station by code.")
    print("5.Get ticket by id.")
    print("6.Get type by id.")
    print("7.Go back.")


def print_response(response):
    if response:
        print(response)
    else:
        print("No data in the response.")


def get_obj_for_train():
    return {
        "departure_station": get_correct_number("Departure station: "),
        "arrival_station": get_correct_number("Arrival station: "),
        "departure_time": input("Departure time(hh:mm::ss): "),
        "arrival_time": input("Arrival time(hh:mm::ss): ")
    }


def get_update_obj_for_train():
    return {
        "train_number": get_correct_number("Train number: "),
        "departure_station": get_correct_number("Departure station: "),
        "arrival_station": get_correct_number("Arrival station: "),
        "departure_time": input("Departure time(hh:mm::ss): "),
        "arrival_time": input("Arrival time(hh:mm::ss): ")
    }


def get_obj_for_station():
    return {
        "code": input("Station code: "),
        "name": input("Station name: ")
    }


def get_obj_for_carriage():
    return {
        "train_number": get_correct_number("Train number: "),
        "carriage_number": get_correct_number("Carriage number: "),
        "type_id": get_correct_number("Type of the carriage: "),
        "seat_count": get_correct_number("Count of seats: ")
    }


def get_obj_for_type():
    return {
        "id": get_correct_number("Input id: "),
        "name": input("Input string designator for the id: ")
    }


def get_obj_for_ticket():
    return {
        "uid": get_correct_number("UID: "),
        "departure_date": input("Date(year-month-day): "),
        "price": get_correct_number("Price: "),
        "name": input("Name: "),
        "surname": input("Surname: ")
    }


def get_update_obj_for_ticket():
    return {
        "ticket_id": get_correct_number("Ticket id: "),
        "uid": get_correct_number("UID: "),
        "departure_date": input("Date(year-month-day): "),
        "price": get_correct_number("Price: "),
        "name": input("Name: "),
        "surname": input("Surname: ")
    }


def get_obj_for_seat():
    return {
        "train_number": get_correct_number("Train number: "),
        "carriage_id": get_correct_number("Carriage id: "),
        "seat_number": get_correct_number("Seat number: "),
        "location": input("Location: ")
    }


def get_update_obj_for_seat():
    return {
        "uid": get_correct_number("UID:" ),
        "train_number": get_correct_number("Train number: "),
        "carriage_id": get_correct_number("Carriage id: "),
        "seat_number": get_correct_number("Seat number: "),
        "location": input("Location: ")
    }


def get_correct_number(string_designator="Your choice: "):
    while True:
        try:
            ch = int(input(string_designator))
        except ValueError:
            print("Try again..")
        else:
            return ch
