from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import requests
import json

# ========== USER SETTINGS ==========
API_KEY = "2b9e051e88f549d509c076e96792f9e2"
CITY = "Karachi"   # you can change city
# ==================================

# AWS IoT setup
client = AWSIoTMQTTClient("weatherClient")

client.configureEndpoint(
    "a15ap37rj8eqx7-ats.iot.us-east-2.amazonaws.com",
    8883
)

client.configureCredentials(
    "rootCA.pem",
    "private.key",
    "certificate.pem.crt"
)

client.connect()
print("Connected to AWS IoT")

# Weather API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

while True:
    try:
        response = requests.get(url)
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        payload = {
            "city": CITY,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather
        }

        client.publish(
            "weather/live",
            json.dumps(payload),
            1
        )

        print("Sent to AWS:", payload)

    except Exception as e:
        print("Error:", e)

    time.sleep(60)   # sends data every 1 minute
