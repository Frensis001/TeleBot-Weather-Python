import requests
import os
from pprint import pprint

TOKEN_API_WEATHER = os.environ["TOKEN_API_WEATHER"]


smail_weather = {
    '01n': '☀'

}


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
    pprint(data)

    if (data["cod"]) == '404':
        return "Есть такой город ?"
    else:
        if (data['weather'][0]['icon']) in smail_weather:
            icon = smail_weather[(data['weather'][0]['icon'])]
        weather = str(data['weather'][0]['description']).capitalize() + icon +\
                  "\nТемпература  " + str(data["main"]["temp"]) + '°C ' + \
                  "\nСкорость ветера  " + str(data["wind"]["speed"]) + ' м/с' + \
                  "\nВлажность  " + str(data["main"]["humidity"]) + '%' + \
                  "\nОблачность " + str(data["clouds"]['all']) + '%'
        return weather
