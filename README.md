# Raspberry-pi-crop-sensor
This project intended to make the first prototype for Solarvibes with a Raspberry Pi 3 connected with a pH, moisture and temperature sensors to monitor soil variables as well as weather data and to assist the first idea of the Agrimodule Smart System.


## Introduction
The idea was to show a prototype in the CUBE TECH FAIR 2017 to explain the idea behind Agrimodule and its benefits for farmers, such as efficient use of resources like water and fertilizer throught irrigation automation and constant field monitoring.


### Raspberry Pi:
This is just a simple repo to connect a couple of sensors to a Rasberry Pi 3 for fast prototyping.
* Soil pH sensor from Atlas Scientific
* Soil moisture & humidity from Chirp sensors
* Air temperature and humidity from SHT31


### Explanation
*  A setting up process comes into place that walk you through the information the script needs in order to set a crop to cultivativate.
* 1. ask for personal information: farm name, location (country, city)
* 2. insert the sensors into the soil to perform reading and give a selection of what suit best for that type of soil base on the crop database in the script
* 3. Asks to check either if user wants to choose their own crop or get suggestions from the system which crop grow best.
* 4. Asks cultivation area: for how many plants or how big is the space for them to grow
* 5. based on data input by user (crop choosen, etc) it calculates predicted yield and water and energy usage throughout the cultivation cycle base on the crop's database within the script
* 6. Asks if you want to start the system (basically starts just reading and displaying the variables monitored by the sensors.
