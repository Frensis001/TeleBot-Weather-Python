import requests
import os

TOKEN_API_WEATHER = os.environ["TOKEN_API_WEATHER"]


def weather_api(City):
    url_api = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': City,
        'appid': TOKEN_API_WEATHER,
        'units': 'metric'

    }
    req = requests.get(url_api, params=params)
    data = req.json()
    print(data)
    if (data["cod"]) == '404':
        print('не верный город')
        return "Не верный город"
    else:
        weather = str(data["main"]["temp"]) + '°C'
        return weather


if __name__ == "__main__":
    weather_api()
