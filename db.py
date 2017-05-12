from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import datetime


engine = create_engine('sqlite:///place.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Place(Base):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    address = Column(String(300))
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String(120))

    def __repr__(self):
        return '<Место: {} {}>'.format(self.name, self.address)
        

def init_db():
    csv_headers = ['name', 'address', 'latitude', 'longitude', 'description']
    Base.metadata.create_all(bind=engine)
    load_data_from_csv('place.csv', Place, True, csv_headers)


def get_all_cafes_from_db():
    cafes_raw = Place.query.all()
    return cafes_raw


def load_data_from_csv(csv_filepath, db_class, do_commit=False, fields=[]):
    with open(csv_filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:
            db_session.add(db_class(**row))
    if do_commit:
        db_session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
