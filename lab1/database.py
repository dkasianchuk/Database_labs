def create_table_train(curr, conn):
    curr.execute("""CREATE TABLE train (
                        train_number SERIAL PRIMARY KEY,
                        departure_station INT,
                        arrival_station INT,
                        departure_time TIME,
                        arrival_time TIME,
                        FOREIGN KEY (departure_station) REFERENCES
                        station (code)
                        ON DELETE CASCADE,
                        FOREIGN KEY (arrival_station) REFERENCES
                        station (code)
                        ON DELETE CASCADE)""")
    conn.commit()


def create_table_station(curr, conn):
    curr.execute("""CREATE TABLE station (
                        code INT PRIMARY KEY,
                        name VARCHAR(20))""")
    conn.commit()


def create_table_carriage(curr, conn):
    curr.execute("""CREATE TABLE carriage (
                        carriage_id SERIAL PRIMARY KEY,
                        train_number INT,
                        carriage_number INT,
                        type_id INT,
                        seat_count INT,
                        FOREIGN KEY (type_id) REFERENCES
                        type (id) 
                        ON DELETE CASCADE,
                        FOREIGN KEY (train_number) REFERENCES
                        train (train_number) 
                        ON DELETE CASCADE )""")
    conn.commit()


def create_table_type(curr, conn):
    curr.execute("""CREATE TABLE type(
                                id INT PRIMARY KEY UNIQUE,
                                name VARCHAR(12))""")
    conn.commit()


def create_table_seat(curr, conn):
    curr.execute("""CREATE TABLE seat (
                                uid SERIAL PRIMARY KEY,
                                carriage_id INT,
                                seat_number INT,
                                location VARCHAR(10),
                                FOREIGN KEY (carriage_id) REFERENCES
                                carriage (carriage_id) 
                                ON DELETE CASCADE)""")
    conn.commit()


def create_table_ticket(curr, conn):
    curr.execute("""CREATE TABLE ticket (
                                ticket_id SERIAL PRIMARY KEY,
                                uid INT,
                                departure_date DATE,
                                price MONEY,
                                name VARCHAR(20),
                                surname VARCHAR(20),
                                FOREIGN KEY (uid) REFERENCES
                                seat (uid)
                                ON DELETE CASCADE)""")
    conn.commit()


def insert_into_train(curr, conn, obj):
    curr.execute(f"""INSERT INTO train (departure_station,arrival_station,departure_time,arrival_time)
                     VALUES ({obj["departure_station"]},
                             {obj["arrival_station"]},
                            '{obj["departure_time"]}',
                            '{obj["arrival_time"]}')""")
    conn.commit()


def insert_into_station(curr, conn, obj):
    curr.execute(f"""INSERT INTO station (code,name)
                     VALUES ({obj["code"]},
                            '{obj["name"]}')""")
    conn.commit()


def insert_into_carriage(curr, conn, obj):
    curr.execute(f"""INSERT INTO carriage (carriage_number,train_number,type_id,seat_count)
                     VALUES ({obj["carriage_number"]},
                             {obj["train_number"]}
                             {obj["type_id"]},
                             {obj["seat_count"]})""")
    conn.commit()


def insert_into_type(curr, conn, obj):
    curr.execute(f"""INSERT INTO type(id,name)
                         VALUES ({obj["id"]},
                                '{obj["name"]}')""")
    conn.commit()


def insert_into_ticket(curr, conn, obj):
    curr.execute(f"""INSERT INTO ticket (uid, departure_date,price,name,surname)
                         VALUES ({obj["uid"]},
                                '{obj["departure_date"]}',
                                 {obj["price"]},
                                '{obj["name"]}',
                                '{obj["surname"]}')""")
    conn.commit()


def insert_into_seat(curr, conn, obj):
    curr.execute(f"""INSERT INTO seat (carriage_id,seat_number,location)
                     VALUES ({obj["carriage_number"]},
                             {obj["seat_number"]},
                            '{obj["location"]}')""")
    conn.commit()


def delete_train(curr, conn, train_number):
    curr.execute(f"""DELETE FROM train WHERE train_number = {train_number}""")
    conn.commit()


def delete_station(curr, conn, code):
    curr.execute(f"""DELETE FROM station WHERE code = {code}""")
    conn.commit()


def delete_carriage(curr, conn, carriage_id):
    curr.execute(f"""DELETE FROM carriage WHERE carriage_number = {carriage_id}""")
    conn.commit()


def delete_type(curr, conn, type_id):
    curr.execute(f"""DELETE FROM type WHERE id = {type_id}""")
    conn.commit()


def delete_ticket(curr, conn, ticket_id):
    curr.execute(f"""DELETE FROM ticket WHERE ticket_id = {ticket_id}""")
    conn.commit()


def delete_seat(curr, conn, uid):
    curr.execute(f"""DELETE FROM seat WHERE uid = {uid}""")
    conn.commit()


def update_train_by_number(curr, conn, data):
    curr.execute(f"""UPDATE train 
                     SET (departure_station,arrival_station,departure_time,arrival_time) = 
                     ({data["departure_station"]},
                      {data["arrival_station"]},
                     '{data["departure_time"]}',
                     '{data["arrival_time"]}')
                     WHERE train_number = {data["train_number"]}""")
    conn.commit()


def update_station_by_code(curr, conn, data):
    curr.execute(f"""UPDATE station
                     SET (name) = ('{data["name"]}')
                     WHERE code = {data["code"]}""")
    conn.commit()


def update_carriage_by_number(curr, conn, data):
    curr.execute(f"""UPDATE carriage 
                     SET (train_number,carriage_number,type_id,seat_count) = 
                     ({data["train_number"]},
                      {data["carriage_number"]}
                      {data["type_id"]},
                      {data["seat_count"]})
                     WHERE carriage_id = {data["carriage_id"]}""")
    conn.commit()


def update_ticket_by_id(curr, conn, data):
    curr.execute(f"""UPDATE ticket 
                     SET (uid,departure_date,price,name,surname) = 
                     ({data["uid"]},
                     '{data["date"]}'
                      {data["price"]},
                     '{data["name"]}',
                     '{data["surname"]}')
                     WHERE ticket_id = {data["ticket_id"]}""")
    conn.commit()


def update_type_by_id(curr, conn, data):
    curr.execute(f"""UPDATE type
                     SET (name) = ('{data["name"]}'')
                     WHERE id = {data["id"]}""")
    conn.commit()


def update_seat_by_id(curr, conn, data):
    curr.execute(f"""UPDATE seat 
                     SET (carriage_id,seat_number,location) = 
                     ({data["carriage_number"]},
                      {data["seat_number"]},
                     '{data["location"]}')
                      WHERE uid = {data["uid"]}""")
    conn.commit()


def get_train_by_number(curr, train_number):
    curr.execute(f"""SELECT * FROM train WHERE train_number = {train_number}""")
    return curr.fetchone()


def get_carriage_by_id(curr, carriage_id):
    curr.execute(f"""SELECT * FROM carriage WHERE carriage_id = {carriage_id}""")
    return curr.fetchone()


def get_type_by_id(curr, type_id):
    curr.execute(f"""SELECT * FROM type WHERE id =  {type_id}""")
    return curr.fetchone()


def get_station_by_code(curr, code):
    curr.execute(f"""SELECT * FROM station WHERE code =  {code}""")
    return curr.fetchone()


def get_ticket_by_id(curr, ticket_id):
    curr.execute(f"""SELECT * FROM ticket WHERE ticket_id = {ticket_id}""")
    return curr.fetchone()


def get_seat_by_uid(curr, uid):
    curr.execute(f"""SELECT * FROM seat WHERE uid = {uid}""")
    return curr.fetchone()


def get_train(curr):
    curr.execute(f"""SELECT * FROM train""")
    return curr.fetchall()


def get_carriage(curr):
    curr.execute(f"""SELECT * FROM carriage""")
    return curr.fetchone()


def get_type_name(curr):
    curr.execute(f"""SELECT * FROM type_name""")
    return curr.fetchone()


def get_type_count(curr):
    curr.execute(f"""SELECT * FROM type_count """)
    return curr.fetchone()


def get_ticket(curr):
    curr.execute(f"""SELECT * FROM ticket""")
    return curr.fetchone()


def get_seat(curr):
    curr.execute(f"""SELECT * FROM seat""")
    return curr.fetchone()


def drop_all_tables(curr, conn):
    curr.execute("""DROP TABLE IF EXISTS train CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS carriage CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS type CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS ticket CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS seat CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS station CASCADE""")
    conn.commit()
