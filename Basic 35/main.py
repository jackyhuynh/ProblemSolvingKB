import requests

QWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6f28ca2af5a05f520a94a7d20b061846"

# Parameter for the API Call
weather_params = {
    "lat": 41.077470,
    "lon": -85.137490,
    "appid": API_KEY,
    "exclude": "current, minutely, daily",
}
# Response get from the API key
response = requests.get(QWM_Endpoint, params=weather_params)

# Response that need for status
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_snow = False

# Get the code for the next 12 hrs
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if 600 <= int(condition_code) <= 622:
        will_snow = True

if will_snow:
    print("It will be snow today")

