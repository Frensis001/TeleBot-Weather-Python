import requests
import os
from pprint import pprint
import datetime

TOKEN_API_WEATHER = os.environ["TOKEN_API_WEATHER"]

smail_weather = {
    '01d': '☀☀☀☀☀', '01n': '☀☀☀☀☀',
    '02d': '🌤🌤🌤🌤🌤', '02n': '🌤🌤🌤🌤🌤',
    '03d': '🌥🌥🌥🌥🌥', '03n': '🌥🌥🌥🌥🌥',
    '04d': '☁☁☁☁☁', '04n': '☁☁☁☁☁',
    '09d': '🌧🌧🌧🌧🌧', '09n': '🌧🌧🌧🌧🌧',
    '10d': '🌦🌦🌦🌦🌦', '10n': '🌦🌦🌦🌦🌦',
    '11d': '🌩🌩🌩🌩🌩', '11n': '🌩🌩🌩🌩🌩',
    '13d': '❄❄❄❄❄', '13n': '❄❄❄❄❄',
    '50d': '🌫🌫🌫🌫🌫', '50n': '🌫🌫🌫🌫🌫',
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
            smail = smail_weather[(data['weather'][0]['icon'])]
        time_rise = datetime.time.fromtimestamp(data["sys"]["sunrise"])
        time_set = datetime.time.fromtimestamp(data["sys"]["sunset"])
        time_day = time_set - time_rise
        weather = str(data['weather'][0]['description']).capitalize() + \
                "\n" + smail + \
                "\nТемпература:  " + str(data["main"]["temp"]) + '°C ' + \
                "\nСкорость ветера:  " + str(data["wind"]["speed"]) + ' м/с' + \
                "\nВлажность:  " + str(data["main"]["humidity"]) + '%' + \
                "\nОблачность: " + str(data["clouds"]['all']) + '%' + \
                "\n Восход сольца: " + str(time_rise) + \
                "Закат солнца: " + str(time_set) + \
                "\nПродолжительность дня: " + str(time_day)

        return weather
