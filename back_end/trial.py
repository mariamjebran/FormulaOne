from seasons import seasons
from methods import Lap_Times
from methods import Pit_Stops
from pit_stops import pit_stops


def create_laptimes_with_driver():
    for driver in seasons[0].get("drivers"):
        Lap_Times.view_race_laps_by_driver({"id": '1078', "driverId": driver.get("driverId"), "stroke": driver.get("color1")})

def create_pit_stops_with_driver():
    pit_stops = {}
    for driver in seasons[0].get("drivers"):
        driverId = driver.get("driverId")
        data = Pit_Stops.view_pit_stops_by_driver({"id": '1078', "driverId": driver.get("driverId")})
        pit_stops[driverId] = data
    return pit_stops


def filter_lap_times_with_pit_stops():
    for pit in pit_stops:
        Lap_Times.update_one_pit_stop(pit.get("raceId"), pit.get("driverId"), pit.get("lap"))
    return

print(create_laptimes_with_driver())
# print(create_pit_stops_with_driver())
# print(filter_lap_times_with_pit_stops())