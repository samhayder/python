import requests
import datetime
import smtplib
import time

MY_LAT = 51.507351
MY_LNG = -0.127758
HOST_MAIL = "smtp.gmail.com"
MY_EMAIL = "sams.seul@gmail.com"
MY_PASSWORD = "ugji mwpp xaig kacr"

# == ISS Station latitude & longitude
def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    # Your position is within +5 or -5 degree in the ISS position
    if MY_LAT +5 >= iss_latitude <= MY_LAT -5 and MY_LNG +5 <= iss_longitude >= MY_LNG -5:
        return True

# == My sunrise & sunset with latitude & longitude
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    now = datetime.datetime.now()
    time_now = now.hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def now_overhead():
    if iss_overhead and is_night:
        with smtplib.SMTP(host=HOST_MAIL) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="sams.seul@hotmail.com",
                msg=f"Subject:Look Up-\n\nISS Station is now overhead."
            )

while True:
    time.sleep(60)
    
    now_overhead()
   