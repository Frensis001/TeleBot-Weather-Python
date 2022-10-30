import requests
import os

TOKEN_API_WEATHER = os.environ["TOKEN_API_WEATHER"]


def weather_api(City):
    url_api = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': City,
        'appid': TOKEN_API_WEATHER,
        'units': 'metric',
        'lang': 'ru'

    }
    req = requests.get(url_api, params=params)
    data = req.json()
    print(data)
    if (data["cod"]) == '404':
        return "Есть такой город ?"
    else:
        weather = "🔥Температура  " + str(data["main"]["temp"]) + '°C ' + \
                  "\n💨Ветер  " + str(data["wind"]["speed"]) + ' м/с' + \
                  "\n💧Влажность  " + str(data["main"]["humidity"]) + '%'
        return weather

