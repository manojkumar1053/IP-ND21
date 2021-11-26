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
        # only print data when the response is not successful
        if response.status_code == 200:
            data = response.json()
            return data['list']
        else:
            return response.status_code


if __name__ == "__main__":
    print(WeatherService.getForecast())
