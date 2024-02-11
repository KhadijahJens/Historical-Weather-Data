# C3 Created a main.py file and created an instance of Weather class to call the methods
from weather import Weather
import database

weather_instance = Weather(52.52, 13.41, 1, 14, 2024, 0, 0, 0,
                        0, 0, 0, 0, 0, 0)

weather_instance.get_mean_temp()
weather_instance.get_max_wind()
weather_instance.get_precip_sum()

if __name__ == "__main__":

    database_url = 'sqlite:///weather_data.db'
    d = database.DatabasePop(database_url)
    d.add_data(weather_instance)
    d.close()
