import requests
from datetime import datetime
from math import fabs
import smtplib
from dotenv import load_dotenv
import os
import time

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# Format response data
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

sun_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_response = requests.get(f"https://api.sunrise-sunset.org/json", params=sun_parameters)
sun_response.raise_for_status()

sun_data = sun_response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    time.sleep(60)
    # My position is within +5 or -5 degrees of the ISS position
    if fabs(MY_LAT - iss_latitude) == 5 or fabs(MY_LONG - iss_latitude) == 5 and time_now == sunset:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:ISS above you\n\nThe ISS is above you in the sky."
        )
        connection.close()
