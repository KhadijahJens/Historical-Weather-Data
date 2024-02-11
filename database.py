from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# C4 Write a class that creates table in SQLite using SQLAlchemy ORM module

base = declarative_base()


class DataTable(base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    lng = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)
    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

# C5 Populated table with weather data


class DatabasePop:

    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        base.metadata.create_all(self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def add_data(self, weather):
        new_add = DataTable(
            lat=weather.lat,
            lng=weather.lng,
            month=weather.month,
            day=weather.day,
            year=weather.year,
            avg_temp=weather.avg_temp,
            min_temp=weather.min_temp,
            max_temp=weather.max_temp,
            avg_wind=weather.avg_wind,
            min_wind=weather.min_wind,
            max_wind=weather.max_wind,
            sum_precip=weather.sum_precip,
            min_precip=weather.min_precip,
            max_precip=weather.max_precip
        )

        self.session.add(new_add)
        self.session.commit()

        # C6 Queries the table and retrieves the data
        query = self.session.query(DataTable)
        for row in query:
            print(f'latitude: {row.lat}')
            print(f'longitude: {row.lng}')
            print(f'average temperature: {row.avg_temp}')
            print(f'minimum temperature: {row.min_temp}')
            print(f'maximum temperature: {row.max_temp}')
            print(f'average wind speed: {row.avg_wind}')
            print(f'minimum wind speed: {row.min_wind}')
            print(f'maximum wind speed: {row.max_wind}')
            print(f'sum precipitation: {row.sum_precip}')
            print(f'minimum precipitation: {row.min_precip}')
            print(f'maximum precipitation: {row.max_precip}')

        self.session.close()

    def close(self):
        self.session.close()
