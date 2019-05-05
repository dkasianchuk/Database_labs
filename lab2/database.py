from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, or_, func, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

# database's entities


class Train(Base):
    __tablename__ = "train"
    train_number = Column(Integer, primary_key=True)
    departure_station = Column(Integer, ForeignKey("station.code"))
    arrival_station = Column(Integer, ForeignKey("station.code"))
    departure_time = Column(Time)
    arrival_time = Column(Time)
    carriage = relationship("Carriage", backref="train")
    dep_station = relationship("Station", foreign_keys=[departure_station], backref="departure_trains")
    arr_station = relationship("Station", foreign_keys=[arrival_station], backref="arrival_trains")

    def __init__(self, departure_station, arrival_station, departure_time, arrival_time):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __repr__(self):
        return f"<Train ({self.train_number},{self.departure_station}, {self.arrival_station}," \
            f"{self.departure_time},{self.arrival_time})>"


class Station(Base):
    __tablename__ = "station"
    code = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Station ({self.code},{self.name})>"


class Carriage(Base):
    __tablename__ = "carriage"
    carriage_id = Column(Integer, primary_key=True)
    train_number = Column(Integer, ForeignKey("train.train_number"))
    carriage_number = Column(Integer)
    type_id = Column(Integer, ForeignKey("type.id"))
    seat_count = Column(Integer)
    type = relationship("Type", backref="carriages")

    def __init__(self, train_number, carriage_number, type_id, seat_count):
        self.train_number = train_number
        self.carriage_number = carriage_number
        self.type_id = type_id
        self.seat_count = seat_count

    def __repr__(self):
        return f"<Carriage ({self.carriage_id},{self.train_number},{self.carriage_number}," \
            f"{self.type_id},{self.seat_count})>"


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Type ({self.id},{self.name})>"


class Seat(Base):
    __tablename__ = "seat"
    uid = Column(Integer, primary_key=True)
    carriage_id = Column(Integer, ForeignKey("carriage.carriage_id"))
    seat_number = Column(Integer)
    location = Column(String)
    carriage = relationship("Carriage", backref="seats")
    ticket = relationship("Ticket", uselist=False, backref="seat")

    def __init__(self, carriage_id, seat_number, location):
        self.carriage_id = carriage_id
        self.seat_number = seat_number
        self.location = location

    def __repr__(self):
        return f"<Seat ({self.uid},{self.carriage_id},{self.seat_number},{self.location})>"


class Ticket(Base):
    __tablename__ = "ticket"
    ticket_id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("seat.uid"))
    departure_date = Column(Date)
    price = Column(Numeric)
    name = Column(String)
    surname = Column(String)

    def __init__(self, uid, departure_date, price, name, surname):
        self.uid = uid
        self.departure_date = departure_date
        self.price = price
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"<Ticket ({self.ticket_id},{self.uid},{self.departure_date},{self.price},{self.name},{self.surname})>"


# database's operations

def insert_into_train(session, obj):
    session.add(Train(obj["departure_station"],
                      obj["arrival_station"],
                      obj["departure_time"],
                      obj["arrival_time"]))
    session.commit()


def insert_into_station(session, obj):
    session.add(Station(obj["name"]))
    session.commit()


def insert_into_carriage(session, obj):
    session.add(Carriage(obj["carriage_number"],
                         obj["train_number"],
                         obj["type_id"],
                         obj["seat_count"]))
    session.commit()


def insert_into_type(session, obj):
    session.add(Type(obj["name"]))
    session.commit()


def insert_into_ticket(session, obj):
    session.add(Ticket(obj["uid"],
                       obj["departure_date"],
                       obj["price"],
                       obj["name"],
                       obj["surname"]))
    session.commit()


def insert_into_seat(session, obj):
    session.add(Seat(obj["carriage_id"],
                     obj["seat_number"],
                     obj["location"]))
    session.commit()


def update_train_by_number(session, data):
    session.query(Train).filter_by(train_number=data["train_number"]).\
        update({"departure_station": data["departure_station"],
                "arrival_station": data["arrival_station"],
                "departure_time": data["departure_time"],
                "arrival_time": data["arrival_time"]})
    session.commit()


def update_station_by_code(session, data):
    session.query(Station).filter_by(code=data["code"]).update({"name": data["name"]})
    session.commit()


def update_carriage_by_number(session, data):
    session.query(Carriage).filter_by(carriage_id=data["carriage_id"]).\
        update({"train_number": data["train_number"],
                "carriage_number": data["carriage_number"],
                "type_id": data["type_id"],
                "seat_count": data["seat_count"]})
    session.commit()


def update_ticket_by_id(session, data):
    session.query(Ticket).filter_by(ticket_id=data["ticket_id"]).update({"uid": data["uid"],
                                                                         "departure_date": data["date"],
                                                                         "price": data["price"],
                                                                         "name": data["name"],
                                                                         "surname": data["surname"]})
    session.commit()


def update_type_by_id(session, data):
    session.query(Type).filter_by(id=data["id"]).update({"name": data["name"]})
    session.commit()


def update_seat_by_id(session, data):
    session.query(Seat).filter_by(uid=data["uid"]).update({"carriage_number": data["carriage_number"],
                                                           "seat_number": data["seat_number"],
                                                           "location": data["location"]})
    session.commit()


def delete_train(session, train_number):
    session.query(Train).filter_by(train_number=train_number).delete()
    session.commit()


def delete_station(session, code):
    session.query(Station).filter_by(code=code).delete()
    session.commit()


def delete_carriage(session, carriage_id):
    session.query(Carriage).filter_by(carriage_id=carriage_id).delete()
    session.commit()


def delete_type(session, type_id):
    session.query(Type).filter_by(type_id=type_id).delete()
    session.commit()


def delete_seat(session, uid):
    session.query(Seat).filter_by(uid=uid).delete()
    session.commit()


def delete_ticket(session, ticket_id):
    session.query(Ticket).filter_by(ticket_id=ticket_id).delete()
    session.commit()


def get_train_by_number(session, train_number):
    query = session.query(Train).filter_by(train_number=train_number)
    return query.one()


def get_carriage_by_id(session, carriage_id):
    query = session.query(Carriage).filter_by(carriage_id=carriage_id)
    return query.one()


def get_type_by_id(session, type_id):
    query = session.query(Type).filter_by(id=type_id)
    return query.one()


def get_station_by_code(session, code):
    query = session.query(Station).filter_by(code=code)
    return query.one()


def get_ticket_by_id(session, ticket_id):
    query = session.query(Ticket).filter_by(ticket_id=ticket_id)
    return query.one()


def get_seat_by_uid(session, uid):
    query = session.query(Seat).filter_by(uid=uid)
    return query.one()


def search_in_interval_train_carriage(session, interval):
    query = session.query(Train.train_number, Carriage.carriage_id)\
        .join(Carriage, Train.train_number == Carriage.train_number)\
        .filter(or_(Train.train_number.between(interval["train_down"], interval["train_up"])),
                   (Carriage.carriage_number.between(interval["carriage_down"], interval["carriage_up"])))
    return query.fetchall()


def search_in_enum(session, enum):
    query = session.query(Type.id).filter(Type.name.in_(enum))
    return query.all()


def drop_all_tables(engine):
    Base.metadata.drop_all(engine)


def create_all_tables(engine):
    Base.metadata.create_all(engine)

# full text search


def full_text_ticket_search(session, word):
    query = session.query(Ticket).filter(or_(Ticket.to_tsvector.op('@@')(func.plainto_tsquery(word)))
                                            (Ticket.to_tsvector.op('@@')(func.plainto_tsquery(word))))
    return query.all()


def full_text_seat_search(session, word):
    query = session.query(Seat)\
        .filter(Seat.location.not_in_(session.query(Seat.location)
                                      .filter(Seat.location.tsvector_op('@@')(func.plainto_tsquery(word)))))
    return query.fetchall()
