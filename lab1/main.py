import psycopg2
from psycopg2.extras import DictCursor
from contextlib import closing


def run(db_name, user='postgres', password='135798642', host='127.0.0.1', port=5433):
    with closing(psycopg2.connect(dbname=db_name,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            drop_all_tables(cursor, conn)
            create_table_type_name(cursor, conn)
            create_table_type_count(cursor, conn)
            create_table_location(cursor, conn)
            create_table_train(cursor, conn)
            create_table_carriage(cursor, conn)
            create_table_ticket(cursor, conn)
            create_table_ticket_info(cursor, conn)


def create_table_train(curr, conn):
    curr.execute("""CREATE TABLE train (
                        train_number SERIAL PRIMARY KEY,
                        departure_station VARCHAR(20) CHECK (departure_station != ''),
                        arrival_station VARCHAR(20) CHECK (arrival_station != ''),
                        carriage_count INTEGER)""")
    conn.commit()


def create_table_carriage(curr, conn):
    curr.execute("""CREATE TABLE carriage (
                        carriage_number INTEGER PRIMARY KEY,
                        type_id INTEGER,
                        FOREIGN KEY (type_id) REFERENCES
                        type_name (type_id))""")
    conn.commit()


def create_table_ticket_info(curr, conn):
    curr.execute("""CREATE TABLE ticket_info (
                                uid INTEGER PRIMARY KEY,
                                train_number INTEGER,
                                carriage_number INTEGER,
                                FOREIGN KEY (uid) REFERENCES
                                ticket (uid),
                                FOREIGN KEY (train_number) REFERENCES
                                train (train_number),
                                FOREIGN KEY (carriage_number) REFERENCES
                                carriage (carriage_number))""")
    conn.commit()


def create_table_type_name(curr, conn):
    curr.execute("""CREATE TABLE type_name (
                                type_id INTEGER PRIMARY KEY UNIQUE,
                                type_str VARCHAR(12))""")
    conn.commit()


def create_table_type_count(curr, conn):
    curr.execute("""CREATE TABLE type_count (
                                type_id INTEGER PRIMARY KEY,
                                count INTEGER,
                                FOREIGN KEY (type_id) REFERENCES
                                type_name (type_id))""")
    conn.commit()


def create_table_location(curr, conn):
    curr.execute("""CREATE TABLE location (
                                seat_number INTEGER PRIMARY KEY,
                                seat_location VARCHAR(4))""")
    conn.commit()


def create_table_ticket(curr, conn):
    curr.execute("""CREATE TABLE ticket (
                                uid SERIAL PRIMARY KEY,
                                seat_number INTEGER,
                                departure_date TIMESTAMP,
                                price INTEGER,
                                FOREIGN KEY (seat_number) REFERENCES
                                location (seat_number))""")
    conn.commit()


def insert_into_train(curr, conn, obj):
    curr.execute(f"""INSERT INTO train (departure_station,arrival_station,carriage_count)
                     VALUES ('{obj["departure_station"]}',
                             '{obj["arrival_station"]}',
                             '{obj["carriage_count"]}')""")
    conn.commit()


def insert_into_carriage(curr, conn, obj):
    curr.execute(f"""INSERT INTO carriage (carriage_number,type_id)
                     VALUES ('{obj["carriage_number"]}',
                             '{obj["id"]}')""")
    conn.commit()


def insert_into_type_name(curr, conn, obj):
    curr.execute(f"""INSERT INTO type_name (type_id,type_str)
                         VALUES ('{obj["id"]}',
                                 '{obj["str"]}')""")
    conn.commit()


def insert_into_type_count(curr, conn, obj):
    curr.execute(f"""INSERT INTO type_count (type_id,count)
                         VALUES ('{obj["id"]}',
                                 '{obj["count"]}')""")
    conn.commit()


def insert_into_location(curr, conn, obj):
    curr.execute(f"""INSERT INTO location (seat_number,seat_location)
                         VALUES ('{obj["number"]}',
                                 '{obj["location"]}')""")
    conn.commit()


def insert_into_ticket(curr, conn, obj):
    curr.execute(f"""INSERT INTO location (seat_number,departure_date,price)
                         VALUES ('{obj["number"]}',
                                 '{obj["date"]}',
                                 '{obj["price"]}')""")
    conn.commit()


def drop_all_tables(curr, conn):
    curr.execute("""DROP TABLE IF EXISTS train CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS carriage CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS train_carriage CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS type_count CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS type_name CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS location CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS ticket CASCADE""")
    curr.execute("""DROP TABLE IF EXISTS ticket_info CASCADE""")
    conn.commit()


if __name__ == "__main__":
    run('db_lab')

