This is a project by group Power Horses from SEEL4213 Software Engineering Section 1

# Plant Monitoring System
####**Table of Contents**  
[Problem Statement](#Problem-Statement)  
[System Architecture](#System-Architecture)   
[Sensors](#Sensors)  
[Cloud Platform](#Cloud-Platform)  
[Dashboard](#Dashboard)  
  

## Problem Statement
In agriculture oriented country such as India, the rate at which water resources are depleting is a dangerous threat. Hence, a smart and efficient way is needed to supply water to the field which has water requirement.
When the cropland are relatively wide, the moisture of the soil may be different. Hence, we think that humidity, temperature and light intensity may be the main factors in designing the system.
In this project, we will use temperature & humidity sensor and ambient light sensor to implement a plant monitoring system that will distribute water to the field which has water requirement.

## System Architecture
![schematic](/images/System_archi.jpeg)

## Sensors
This project involves the usage of DHT-11 Temperature & Humidty Sensor to collect data regarding surrounding humidity and temperature and BH1750 Ambient Light Sensor to collect data regarding the
surrounding lighting conditions. Both of the sensors will be connected to a ESP8266 WiFi module for control purposes and also for uploading their data to the cloud platform via HTTP communication
protocol. Following figure shows the connections of the sensors and the ESP8266 WiFi module.  

![schematic](/images/schematic_diagram.png)

Parts Used :  
1. DHT-11 Temperature & Humidity Sensor
2. BH1750 Ambient Light Sensor
3. ESP8266 WiFi Module  

References : 
1. https://techatronic.com/interfacing-of-dht11-sensor-with-esp8266-nodemcu/
2. https://randomnerdtutorials.com/esp8266-nodemcu-bh1750-ambient-light-sensor/

## Cloud Platform
The sensors data will be uploaded to a Django application hosted by PythonAnywhere. Following is a sample Django application that prints "Hello!" on browser hosted by PythonAnywhere.  
  
[Link to video demo](https://youtu.be/fbEuLwPSxxY)  
  

The Django application hosted will be displaying the dashboard containing the information from the sensors connecting to the ESP8266 WiFi module.  

## Dashboard 
