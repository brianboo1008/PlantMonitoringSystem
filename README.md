This is a project by group Power Horses from SEEL4213 Software Engineering Section 1

# Plant Monitoring System
**Table of Contents**
### Problem Statement
### System Acrhitecture 
### Sensors
### Cloud Platform
### Dashboard

## Problem Statement


## System Architecture


## Sensors
This project involves the usage of DHT-11 Temperature & Humidty Sensor to collect data regarding surrounding humidity and temperature and BH1750 Ambient Light Sensor to collect data regarding the
surrounding lighting conditions. Both of the sensors will be connected to a ESP8266 WiFi module for control purposes and also for uploading their data to the cloud platform via HTTP communication
protocol. Following figure shows the connections of the sensors and the ESP8266 WiFi module.

![schematic](/images/schematic_diagram.png)

Parts Used :	 DHT-11 Temperature & Humidity Sensor
		 BH1750 Ambient Light Sensor
		 ESP8266 WiFi Module

References : 
1. https://techatronic.com/interfacing-of-dht11-sensor-with-esp8266-nodemcu/
2. https://randomnerdtutorials.com/esp8266-nodemcu-bh1750-ambient-light-sensor/

## Cloud Platform
The sensors data will be uploaded to a Django application hosted by PythonAnywhere. Following is a sample Django application that prints "Hello!" on browser hosted by PythonAnywhere.


## Dashboard 
