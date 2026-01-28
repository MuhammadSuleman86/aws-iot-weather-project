# AWS IoT Weather Monitoring Project

## Project Overview
This project demonstrates how a **virtual IoT device** built using **Python** sends
**real-time weather data** to **AWS IoT Core** using **MQTT** and **X.509 certificates**.

No physical hardware is used. Python acts as an IoT device.

---

## Technologies Used
- Python
- AWS IoT Core
- MQTT Protocol
- Free Weather API
- X.509 Certificates

---

## How It Works
1. Python script fetches weather data from a free API
2. Data is formatted in JSON
3. A secure MQTT connection is established using certificates
4. Data is published to AWS IoT Core topic
5. AWS IoT Core receives and logs the data

---

## Project Structure
