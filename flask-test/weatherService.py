# weatherService.py

import requests


class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = ''
    with open('../api_key.txt', 'r') as f:
        appId = f.read().strip()

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
        ])

        data = response.json()

        return data['list']


if __name__ == "__main__":
    print(WeatherService.getForecast())
