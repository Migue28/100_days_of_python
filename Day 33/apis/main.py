import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

# Format response data
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
position = (latitude, longitude)

print(position)
