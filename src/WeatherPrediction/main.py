import requests
from twilio.rest import Client
import os

QWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "put your API key here"
account_sid = 'ACb7130c56bbacc92bd1067ed578ca0173'
auth_token = 'put Authorize code here'

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
    if 801 <= int(condition_code) <= 804:
        will_snow = True

if will_snow:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It will be snow today",
        from_="+13208558019",
        to="+14088963449"
    )
    print(message.status)
