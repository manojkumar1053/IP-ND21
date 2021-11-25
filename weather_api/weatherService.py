import requests


class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = ''

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
        ])

        data = response.json()
        if data:
            return data['list']
        else:
            return None


if __name__ == "__main__":
    print(WeatherService.getForecast())

# To test API Request
