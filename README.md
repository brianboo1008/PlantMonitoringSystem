This is a project by group Power Horses from SEEL4213 Software Engineering Section 1

# Greenhouse Monitoring System
##**Table of Contents**  
[Problem Statement](#Problem-Statement)  
[System Architecture](#System-Architecture)   
[Sensors](#Sensors)  
[Cloud Platform](#Cloud-Platform)  
[Dashboard](#Dashboard)  
[Relational Database Table](#Relational-Database-Table)  
[Results](#Results)  
  

## Problem Statement
In agriculture oriented country such as India, the rate at which water resources are depleting is a dangerous threat. Hence, a smart and efficient way is needed for certain plant that are more sensitive to external environment. Some non-native crop could have altered transpiration rate depending on air humidity, sunlight exposure and temperature.
As per requirement, the moisture of the air may be different. Hence, we think that humidity, temperature and light intensity may be the main factors in designing the system that can provide biological input to the crop to control the growth of that crop
In this project, we will use temperature & humidity sensor and ambient light sensor to implement a plant monitoring system that will distribute water to the field which has water requirement.

## System Architecture
![schematic](/images/archi.jpg)
The sensor infomation will be transmitted to a Python/Django Application using ESP32. Then the application data will be stored into MySQL Database. Lastly, using a dashboard of our choice, the data will be display on the Dashboard.

## Sensors
This project involves the usage of DHT-11 Temperature & Humidty Sensor to collect data regarding surrounding humidity and temperature, BH1750 Ambient Light Sensor to collect data regarding the surrounding lighting conditions and MH-RD raindrop Sensor Module to sense the present of rain. All of the sensors will be connected to a ESP8266 WiFi module for control purposes and also for uploading their data to the cloud platform via HTTP communication protocol. Following figure shows the connections of the sensors and the ESP8266 WiFi module.  

![schematic](/images/schematic.jpg)

Parts Used :  
1. DHT-11 Temperature & Humidity Sensor
2. BH1750 Ambient Light Sensor
3. MH-RD Raindrop Sensor Module
4. ESP8266 WiFi Module  

References : 
1. https://techatronic.com/interfacing-of-dht11-sensor-with-esp8266-nodemcu/
2. https://randomnerdtutorials.com/esp8266-nodemcu-bh1750-ambient-light-sensor/

## Cloud Platform
The sensors data will be uploaded to a Django application hosted by PythonAnywhere. Following is a sample Django application that prints "Hello!" on browser hosted by PythonAnywhere.  
  
[Link to video demo](https://youtu.be/fbEuLwPSxxY)  
  

The Django application hosted will be displaying the dashboard containing the information from the sensors connecting to the ESP8266 WiFi module.  

## Dashboard 

<p align="center">
  <img src="https://user-images.githubusercontent.com/83630228/204231158-b9610a2b-2a21-4fd5-b2ed-c2791a1343a8.png" alt="PlantMonitoringDashboard"/>
</p>

   The Greenhouse Monitoring Dashboad is connected to the Arduino IoT Device through the intermediate cloud interface. There are 2 cluster of dashboards meant to provide monitoring to 4 variables that is light intensity, temperature, humidity and the presence of raindrop. Each variable come with a chart that will collect and display the data overtime to provide better grasp on the evironment of the plant. The sensor is set to be collecting the data on fix time interval to reduce power consumption of the device.
   With each dashboard there is an option as well to control the artificial sunlight and watering system. A scheduler is also implemented to provide automatic management onto the device above.

## Relational Database Table 

The realtional database table of the system is shown below.
![schematic](/images/dbmstable.jpg)

## Results 

The results below shows the website interface of the system. In this wesite, the user can choose to view the data for the Dry Weather of the Rain Weather. Both of the charts shows the data for the light intensity, humidity and the temperature measurement collected from the sensors.The data are shown in a chart form so that the change or the trends of the data are more visible.  
![schematic](/images/dryweather.png)
![schematic](/images/rainningweather.png)
