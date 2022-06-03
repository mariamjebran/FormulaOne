import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
# from lap_times import lap_times
from drivers import drivers
from seasons import seasons
# from pit_stops import pit_stops

Base = declarative_base()

class Drivers(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "drivers"

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String)
    number = Column(String)
    code = Column(String)
    forename = Column(String)
    surname = Column(String)
    dob = Column(String)
    nationality = Column(String)
    url = Column(String)

    @classmethod
    def insert_csv(cls):
        with open('drivers.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Drivers(driverId=row[0], driverRef=row[1], number=row[2], code=row[3], forename=row[4],
                    surname=row[5], dob=row[6], nationality=row[7], url=row[8])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"driverId":self.driverId,"forename": self.forename, "surname": self.surname })
        # return({"driverId":self.driverId,"driverRef": self.driverRef, "number": self.number, "code": self.code,
        #     "forename": self.forename, "surname": self.surname,
        #     "dob": self.dob, "nationality": self.nationality,
        #     "url": self.url})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            drivers = select(Drivers)
            for driver in session.scalars(drivers): 
                list.append(driver.to_json())
            return list
    
    @classmethod
    def view_driver(cls,data):
        with Session(cls.engine) as session:
            drivers = select(Drivers).where(Drivers.driverId == data.get("id"))
            list = []
            for driver in session.scalars(drivers):
                list.append(driver.to_json())
            return list

class Constructors(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "constructors"

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String)
    name = Column(String)
    nationality = Column(String)
    url = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('constructors.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Constructors(constructorId=row[0], constructorRef=row[1], name=row[2], nationality=row[3], url=row[4])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"constructorId":self.constructorId,"constructorRef": self.constructorRef, "name": self.name, "nationality": self.nationality,
            "url": self.url})
    
    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            constructors = select(Constructors)
            for constructor in session.scalars(constructors): 
                list.append(constructor.to_json())
            return list

class Circuits(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "circuits"

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    lat = Column(String)
    lng = Column(String)
    alt = Column(String)
    url = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('circuits.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Circuits(circuitId=row[0], circuitRef=row[1],
                    name=row[2], location=row[3], country=row[4], lat=row[5],
                    lng=row[6], alt=row[7], url=row[8])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"circuitId":self.circuitId,"circuitRef": self.circuitRef,
                "name": self.name, "location": self.location, 
                "country": self.country, "lat": self.lat, "lng": self.lng,
                "alt": self.alt, "url": self.url})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            circuits = select(Circuits)
            for circuit in session.scalars(circuits): 
                list.append(circuit.to_json())
            return list

class Races(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "races"

    raceId = Column(Integer, primary_key=True)
    year = Column(String)
    round = Column(String)
    circuitId = Column(String)
    name = Column(String)
    date = Column(String)
    time = Column(String)
    url = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('races.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Races(raceId=row[0], year=row[1],
                    round=row[2], circuitId=row[3], name=row[4], date=row[5],
                    time=row[6], url=row[7])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"raceId":self.raceId, "name": self.name, "date": self.date})
        # return({"raceId":self.raceId,"year": self.year,
        #         "round": self.round, "circuitId": self.circuitId, 
        #         "name": self.name, "date": self.date, "time": self.time,
        #         "url": self.url})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            races = select(Races)
            for race in session.scalars(races): 
                list.append(race.to_json())
            return list
    
    @classmethod
    def view_race(cls, data):
        with Session(cls.engine) as session:
            races = select(Races).where(Races.raceId == data.get("id"))
            list = []
            for race in session.scalars(races):
                list.append(race.to_json())
            return list


class Lap_Times(Base):

    dbpath = "./formula_one.db"

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "lap_times"
    id = Column(Integer, primary_key = True)
    raceId = Column(Integer)
    driverId = Column(String)
    lap = Column(String)
    position = Column(String)
    time = Column(String)
    milliseconds = Column(String)
    time_in_seconds = Column(Integer)
    pit_stop = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('lap_times.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                count = 0
                for row in csv_reader[1:]:
                    row = row.split(',')
                    minutes,seconds = row[4].split(":")
                    time_in_seconds = int(minutes)*60 + float(seconds)
                    data = Lap_Times(id=count,raceId=row[0], driverId=row[1],
                    lap=row[2], position=row[3], time=row[4],
                    milliseconds=row[5], time_in_seconds = time_in_seconds, pit_stop = False) 
                    count += 1
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"raceId":self.raceId,"driverId": self.driverId,                                                                                                                                   
                "lap": self.lap, "time_in_seconds":self.time_in_seconds, "pit_stop": self.pit_stop})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            laps = select(Lap_Times)
            for lap in session.scalars(laps): 
                list.append(lap.to_json())
            return list

    @classmethod
    def view_race_laps(cls,data):
        with Session(cls.engine) as session:
            laps = select(Lap_Times).where(Lap_Times.raceId == data.get("id"))
            list = []
            for lap in session.scalars(laps):
                list.append(lap.to_json()) #if object 
            return list

    @classmethod
    def view_race_laps_by_driver(cls,data):
        new_data = {"name": "", "data": [], "stroke": ""}
        new_data["name"] = data.get("surname")
        new_data["stroke"] = data.get("stroke")
        with Session(cls.engine) as session:
            laps = select(Lap_Times).where(Lap_Times.raceId == data.get("race_id")).where(Lap_Times.driverId == data.get("driver_id"))
            for lap in session.scalars(laps):
                new_data.get("data").append(lap.to_json())
        return new_data

    @classmethod
    def update_pit_stop(cls, pit_stops):
        # pit_stops = Pit_Stops.view_all()
        for pit in pit_stops:
            Lap_Times.update_one_pit_stop__(pit.get("raceId"), pit.get("driverId"), pit.get("lap"))
    
    @classmethod
    def update_one_pit_stop(cls, raceId, driverId, lap):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = """UPDATE lap_times SET pit_stop=? WHERE raceId=? AND driverId=? AND lap=?;"""
            cursor.execute(sql, (True, raceId, driverId, lap))
            print("working")
    
    @classmethod
    def testing_update(cls, raceId, driverId, lap):
        with Session(cls.engine) as session:
            laps = select(Lap_Times).where(Lap_Times.raceId == raceId).where(Lap_Times.driverId == driverId).where(Lap_Times.lap == lap)
            for lap in session.scalars(laps):
                print(lap.to_json())
    
    # @classmethod
    # def update_pit_stop(cls, raceId):
    #     pit_stops = Pit_Stops.view_pit_stops_by_driver(raceId)
    #     print(pit_stops)
    #     for driverId, value in pit_stops.items():
    #         Lap_Times.update_pit_stop__(1078, driverId, value.get("pit_stops") )
    #     return ("works")




class Results(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "results"

    resultId = Column(Integer, primary_key=True)
    raceId = Column(String)
    driverId = Column(String)
    constructorId = Column(String)
    number = Column(String)
    grid = Column(String)
    position = Column(String)
    positionText = Column(String)
    positionOrder = Column(String)
    points = Column(String)
    laps = Column(String)
    time = Column(String)
    milliseconds = Column(String)
    fastestLap = Column(String)
    rank = Column(String)
    fastestLapTime = Column(String)
    fastestLapSpeed = Column(String)
    statusId = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('results.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Results(resultId=row[0], raceId=row[1],
                    driverId=row[2], constructorId=row[3], number=row[4],
                    grid=row[5], position = row[6], positionText = row[7],
                    positionOrder = row[8], points = row[9], laps = row[10],
                    time = row[11], milliseconds = row[12], fastestLap = row[13], 
                    rank = row[14], fastestLapTime = row[15], fastestLapSpeed = row[16],
                    statusId = row[17])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"resultId":self.resultId,"raceId": self.raceId,
                "driverId": self.driverId, "constructorId": self.constructorId, 
                "number": self.number, "grid": self.grid, "position": self.position,
                "positionText": self.positionText, "positionOrder": self.positionOrder,
                "points": self.points, "laps": self.laps, "time": self.time,
                "milliseconds": self.milliseconds, "fastestLap": self.fastestLap, 
                "rank": self.rank, "fastestLapTime": self.fastestLapTime, 
                "fastestLapSpeed": self.fastestLapSpeed, "statusId": self.statusId})
    
    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            results = select(Results)
            for result in session.scalars(results): 
                list.append(result.to_json())
            return list

class Driver_Standings(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "driver_standings"

    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(String)
    driverId = Column(String)
    points = Column(String)
    position = Column(String)
    positionText = Column(String)
    wins = Column(String)
 
    @classmethod
    def insert_csv(cls):
        with open('driver_standings.csv','r') as file:
            with Session(cls.engine) as session:
                csv_reader = [line.rstrip('\n') for line in file]
                for row in csv_reader[1:]:
                    row = row.split(',')
                    data = Driver_Standings(driverStandingsId=row[0], raceId=row[1],
                    driverId=row[2], points=row[3], position=row[4],
                    positionText=row[5], wins = row[6])
                    session.add(data)
                session.commit()

    def to_json(self):
        return({"driverStandingsId":self.driverStandingsId,"raceId": self.raceId,
                "driverId": self.driverId, "points": self.points, 
                "position": self.position, "positionText": self.positionText,
                "position": self.position, "wins": self.wins})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            standings = select(Driver_Standings)
            for standing in session.scalars(standings): 
                list.append(standing.to_json())
            return list

class Status(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "status"

    statusId = Column(Integer, primary_key=True)
    status = Column(String)
 
    @classmethod
    def insert_csv(cls):
      with open('status.csv','r') as file:
        with Session(cls.engine) as session:
            csv_reader = [line.rstrip('\n') for line in file]
            for row in csv_reader[1:]:
                row = row.split(',')
                data = Status(statusId=row[0], status=row[1])
                session.add(data)
            session.commit()

    def to_json(self):
        return({"statusId":self.statusId, "status": self.status})

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            list = []
            statuses = select(Status)
            for status in session.scalars(statuses): 
                list.append(status.to_json())
            return list

class Pit_Stops(Base):

    engine = create_engine('sqlite:///formula_one.db', echo=True)
    __tablename__ = "pit_stops"

    count = Column(Integer, primary_key=True)
    raceId = Column(Integer)
    driverId = Column(String)
    stop = Column(String)
    lap = Column(String)
    time = Column(String)
    duration = Column(String)
    milliseconds = Column(String)

    @classmethod
    def insert_csv(cls):
      with open('pit_stops.csv','r') as file:
        with Session(cls.engine) as session:
            i = 0
            csv_reader = [line.rstrip('\n') for line in file]
            for row in csv_reader[1:]:
                row = row.split(',')
                data = Pit_Stops(count = i, raceId=row[0], driverId=row[1], stop=row[2], lap=row[3], time=row[4], 
                                 duration=row[5], milliseconds=row[6])
                session.add(data)
                i += 1
            session.commit()

    def to_json(self):
        return({"raceId":self.raceId, "driverId": self.driverId, "lap": self.lap})
        # return(self.lap)

    @classmethod
    def view_all(cls):
        with Session(cls.engine) as session:
            laps = select(Pit_Stops)
            f= open("pit_stops.txt","a")
            for lap in session.scalars(laps): 
                lap = lap.to_json()
                f.write(str(lap) +",")
            f.close()

    @classmethod
    def view_pit_stops_by_driver__(cls, data):
        driverId = int(data.get("driverId"))
        driver_data = drivers[driverId-1]
        new_data = {"name": "", "pit_stops": []}
        new_data["name"] = driver_data.get("forename") + driver_data.get("surname")
        with Session(cls.engine) as session:
            pit_stops = select(Pit_Stops).where(Pit_Stops.raceId == data.get("id")).where(Pit_Stops.driverId == data.get("driverId"))
            for pit_stop in session.scalars(pit_stops):
                print(pit_stop.to_json())
                new_data.get("pit_stops").append(pit_stop.to_json())
            data[driverId] = new_data
        # f= open("pit_stops.txt","a")
        # f.write(str(new_data) + ",")
        # f.close()
        return new_data

    @classmethod
    def view_pit_stops_by_driver(cls, raceId):
        pit_stops = {}
        for driver in seasons[0].get("drivers"):
            driverId = driver.get("driverId")
            data = Pit_Stops.view_pit_stops_by_driver__({"id": raceId, "driverId": driver.get("driverId")})
            pit_stops[driverId] = data
        return pit_stops



if __name__ == "__main__":
    # print(Drivers.insert_csv())
    # print(Drivers.view_all())
    # print(Drivers.view_driver({"id": '832'}))
    
    # print(Constructors.insert_csv())
    # print(Constructors.view_all())

    # print(Circuits.insert_csv())
    # print(Circuits.view_all())

    # print(Races.insert_csv())
    # print(Races.view_all())
    # print(Races.view_race({"id": '1078'}))

    # print(Lap_Times.insert_csv())
    # print(Lap_Times.view_all())
    print(Lap_Times.view_race_laps_by_driver({"race_id": 1053,"driver_id": 847,
                                                       "stroke": "#8fdad6",
                                                       "surname": "Russell"}))
    # print(Lap_Times.update_pit_stop([{'raceId': 966, 'driverId': 817, 'lap': 1}, {'raceId': 966, 'driverId': 835, 'lap': 1}, {'raceId': 966, 'driverId': 828, 'lap': 1}, {'raceId': 966, 'driverId': 154, 'lap': 11}, {'raceId': 966, 'driverId': 830, 'lap': 12}, {'raceId': 966, 'driverId': 832, 'lap': 12}, {'raceId': 966, 'driverId': 825, 'lap': 12}, {'raceId': 966, 'driverId': 821, 'lap': 12}, {'raceId': 966, 'driverId': 826, 'lap': 13}, {'raceId': 966, 'driverId': 807, 'lap': 14}, {'raceId': 966, 'driverId': 13, 'lap': 14}, {'raceId': 966, 'driverId': 839, 'lap': 15}, {'raceId': 966, 'driverId': 4, 'lap': 16}, {'raceId': 966, 'driverId': 1, 'lap': 17}, {'raceId': 966, 'driverId': 18, 'lap': 17}, {'raceId': 966, 'driverId': 822, 'lap': 19}, {'raceId': 966, 'driverId': 3, 'lap': 20}, {'raceId': 966, 'driverId': 8, 'lap': 20}, {'raceId': 966, 'driverId': 815, 'lap': 20}, {'raceId': 966, 'driverId': 20, 'lap': 32}, {'raceId': 966, 'driverId': 8, 'lap': 45}, {'raceId': 966, 'driverId': 4, 'lap': 45}, {'raceId': 966, 'driverId': 826, 'lap': 47}, {'raceId': 966, 'driverId': 821, 'lap': 48}, {'raceId': 966, 'driverId': 831, 'lap': 49}, {'raceId': 966, 'driverId': 817, 'lap': 50}, {'raceId': 966, 'driverId': 154, 'lap': 50}, {'raceId': 966, 'driverId': 825, 'lap': 51}]))
    # # print(Lap_Times.testing_update('1078', '844', 24))
    # print(Lap_Times.view_race_laps_by_driver({"id": '1078', "driverId": '844'}))
    # print(Lap_Times.update_one_pit_stop('1078', '844','24'))

    # print(Results.insert_csv())
    # print(Results.view_all())

    # print(Driver_Standings.insert_csv())
    # print(Driver_Standings.view_all())

    # print(Status.insert_csv())
    # print(Status.view_all())

    # print(Pit_Stops.insert_csv())
    # print(Pit_Stops.view_all())
    # print(Pit_Stops.view_pit_stops_by_driver(1078))
