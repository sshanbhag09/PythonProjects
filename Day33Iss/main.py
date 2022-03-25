import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 29.3998 # Your latitude
MY_LONG = -36.4190 # Your longitude
def iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True
#Your position is within +5 or -5 degrees of the ISS position.

def sunset_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now<=sunrise and time_now>=sunset:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if iss_near() and sunset_sunrise():
        my_email="appbreweryinfosushant@gmail.com"
        password="RGSS0103sus@"
        email1="appbrewerrtestingsus@yahoo.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email,password=password)
             connection.sendmail(from_addr=my_email,to_addrs=email1,msg=f"Subject:ISS\n\nLook up ISS")



