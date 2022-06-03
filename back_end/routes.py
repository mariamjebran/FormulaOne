from flask import Flask, request, jsonify
from flask_cors import CORS
from methods import Drivers
from methods import Races
from methods import Lap_Times
from lap_times import lap_times
from seasons import seasons
# from pit_stops import pit_stops

app = Flask(__name__)
CORS(app)

@app.route("/view_driver", methods=["POST"])
def view_driver():
    data = request.get_json()
    driver_data = Drivers.view_driver(data) 
    return jsonify(driver_data)

@app.route("/view_race", methods=["POST"])
def view_race():
    data = request.get_json()
    race_data = Races.view_race(data) 
    return jsonify(race_data)

@app.route("/view_lap_times", methods=["POST"])
def view_lap_times():
    data = request.get_json()
    lap_time_data = Lap_Times.view_race_laps(data) 
    return jsonify(lap_time_data)

@app.route("/view_lap_times_by_driver", methods=["POST"])
def view_lap_times_by_driver():
    data = request.get_json()
    drivers_laps = []
    for driver in data.get("drivers"):
        new_data = Lap_Times.view_race_laps_by_driver({"race_id": data.get("raceId"),
                                                       "driver_id": driver.get("driverId"),
                                                       "stroke": driver.get("color1"),
                                                       "surname": driver.get("surname")})
        drivers_laps.append(new_data)
    return jsonify(drivers_laps)

@app.route("/view_seasons", methods=["POST"])
def view_seasons():
    return jsonify(seasons)


if __name__ == "__main__":
    app.run()

