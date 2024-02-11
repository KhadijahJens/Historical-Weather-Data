import requests

# C1 Created a class with the instance variables for chosen location and date


class Weather:
    def __init__(self, lat, lng, month, day, year, avg_temp, min_temp, max_temp,
                 avg_wind, min_wind, max_wind, sum_precip, min_precip, max_precip):
        self.lat = lat
        self.lng = lng
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp = avg_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.avg_wind = avg_wind
        self.min_wind = min_wind
        self.max_wind = max_wind
        self.sum_precip = sum_precip
        self.min_precip = min_precip
        self.max_precip = max_precip

    year = 2024
    month = 1
    day = 14
    date = f'{year}-{month}-{day}'

    # C2 method for each weather variable pull data for your chosen location and date

    def get_mean_temp(self):
        temp_list = []

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2024-01-14&end_date=2024-01-14&daily=temperature_2m_mean&temperature_unit'
               '=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['temperature_2m_mean'][0]
        temp_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2023-01-14&end_date=2023-01-14&daily=temperature_2m_mean&temperature_unit'
               '=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['temperature_2m_mean'][0]
        temp_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2022-01-14&end_date=2022-01-14&daily=temperature_2m_mean&temperature_unit'
               '=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['temperature_2m_mean'][0]
        temp_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2021-01-14&end_date=2021-01-14&daily=temperature_2m_mean&temperature_unit'
               '=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['temperature_2m_mean'][0]
        temp_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2020-01-14&end_date=2020-01-14&daily=temperature_2m_mean&temperature_unit'
               '=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['temperature_2m_mean'][0]
        temp_list.append(data)

        self.avg_temp = sum(temp_list)/len(temp_list)
        self.min_temp = min(temp_list)
        self.max_temp = max(temp_list)

    def get_max_wind(self):
        wind_list = []
        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2024-01-14&end_date=2024-01-14&daily=wind_speed_10m_max&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['wind_speed_10m_max'][0]
        wind_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2023-01-14&end_date=2023-01-14&daily=wind_speed_10m_max&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['wind_speed_10m_max'][0]
        wind_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2022-01-14&end_date=2022-01-14&daily=wind_speed_10m_max&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['wind_speed_10m_max'][0]
        wind_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2021-01-14&end_date=2021-01-14&daily=wind_speed_10m_max&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['wind_speed_10m_max'][0]
        wind_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2020-01-14&end_date=2020-01-14&daily=wind_speed_10m_max&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['wind_speed_10m_max'][0]
        wind_list.append(data)

        self.avg_wind = sum(wind_list)/len(wind_list)
        self.min_wind = min(wind_list)
        self.max_wind = max(wind_list)

    def get_precip_sum(self):
        precip_list = []
        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2024-01-14&end_date=2024-01-14&daily=precipitation_sum&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['precipitation_sum'][0]
        precip_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2023-01-14&end_date=2023-01-14&daily=precipitation_sum&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['precipitation_sum'][0]
        precip_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2022-01-14&end_date=2022-01-14&daily=precipitation_sum&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['precipitation_sum'][0]
        precip_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2021-01-14&end_date=2021-01-14&daily=precipitation_sum&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['precipitation_sum'][0]
        precip_list.append(data)

        url = ('https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41'
               '&start_date=2020-01-14&end_date=2020-01-14&daily=precipitation_sum&temperature_unit=fahrenheit&'
               'wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago')
        response = requests.get(url)
        data_response = response.json()
        daily_data = data_response['daily']
        data = daily_data['precipitation_sum'][0]
        precip_list.append(data)

        self.sum_precip = sum(precip_list)
        self.min_precip = min(precip_list)
        self.max_precip = max(precip_list)
