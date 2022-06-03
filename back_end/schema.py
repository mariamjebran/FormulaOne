from xmlrpc.client import Boolean
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///formula_one.db', echo=True)
Base = declarative_base()

# metadata = MetaData()
# my_table = Table('drivers', metadata,
#     Column('driverId', Integer),
#     Column('driverRef', String),
#     Column('number', String),
#     Column('code', String),
#     Column('forename', String),
#     Column('surname', String),
#     Column('dob', String),
#     Column('nationality', String),
#     Column('url', String)
# )

# metadata = MetaData()
# my_table = Table('constructors', metadata,
#     Column('constructorId', Integer),
#     Column('constructorRef', String),
#     Column('name', String),
#     Column('nationality', String),
#     Column('url', String)
# )

# metadata = MetaData()
# my_table = Table('circuits', metadata,
#     Column('circuitId', Integer),
#     Column('circuitRef', String),
#     Column('name', String),
#     Column('location', String),
#     Column('country', String),
#     Column('lat', String),
#     Column('lng', String),
#     Column('alt', String),
#     Column('url', String)
# )

# metadata = MetaData()
# my_table = Table('races', metadata,
#     Column('raceId', Integer),
#     Column('year', String),
#     Column('round', String),
#     Column('circuitId', String),
#     Column('name', String),
#     Column('date', String),
#     Column('time', String),
#     Column('url', String)
# )

metadata = MetaData()
my_table = Table('lap_times', metadata,
    Column('id', Integer),
    Column('raceId', Integer),
    Column('driverId', String),
    Column('lap', String),
    Column('position', String),
    Column('time', String),
    Column('milliseconds', String),
    Column('time_in_seconds',Integer),
    Column('pit_stop', String)
)

# metadata = MetaData()
# my_table = Table('status', metadata,
#     Column('statusId', Integer),
#     Column('status', String)
# )

# metadata = MetaData()
# my_table = Table('results', metadata,
#     Column('resultId', Integer),
#     Column('raceId', String),
#     Column('driverId', String),
#     Column('constructorId', String),
#     Column('number', String),
#     Column('grid', String),
#     Column('position', String),
#     Column('positionText', String),
#     Column('positionOrder', String),
#     Column('points', String),
#     Column('laps', String),
#     Column('time', String),
#     Column('milliseconds', String),
#     Column('fastestLap', String),
#     Column('rank', String),
#     Column('fastestLapTime', String),
#     Column('fastestLapSpeed', String),
#     Column('statusId', String)
# )

# metadata = MetaData()
# my_table = Table('driver_standings', metadata,
#     Column('driverStandingsId', Integer),
#     Column('raceId', String),
#     Column('driverId', String),
#     Column('points', String),
#     Column('position', String),
#     Column('positionText', String),
#     Column('wins', String)
# )

# metadata = MetaData()
# my_table = Table('pit_stops', metadata,
#     Column('count', Integer),
#     Column('raceId', Integer),
#     Column('driverId', Integer),
#     Column('stop', Integer),
#     Column('lap', Integer),
#     Column('time', String),
#     Column('duration', Integer),
#     Column('milliseconds', Integer)
# )

metadata.create_all(engine)

