import requests

QWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6f28ca2af5a05f520a94a7d20b061846"

weather_params = {
    "lat": 41.077470,
    "lon": -85.137490,
    "appid": API_KEY,
}

response = requests.get(QWM_Endpoint, params=weather_params)
# print(response.status_code)
print(response.json())
