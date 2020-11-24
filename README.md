# WeatherPi
Raspberry Pi based wether station

## Install Process
- New image of Raspian Lite with no applications or desktop
  - Enable SSH
  - Enable I2C
  
### Install the following
- Node.JS and NPM https://www.instructables.com/Install-Nodejs-and-Npm-on-Raspberry-Pi/ sudo apt install build-essential git first to ensure npm is able to build any binary modules it needs to install
- pip
- VEML6075 library https://github.com/pimoroni/veml6075-python
- I2S mic https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test
- `pip install sounddevice==0.3.15`
- Pimoroni Enviro Libraries https://github.com/pimoroni/enviroplus-python
- Node-Red https://nodered.org/docs/getting-started/local

  #### Install the following Nodes
  - DHt22
  - Node-Red-Dashboard
  - node-red-node-pi-mcp3008
  - node-red-contrib-python-function
  - node-red-contrib-counter
  - node-red-contrib-bme280
  - node-red-contrib-msg-speed
  - node-red-contrib-msg-speed

### On Primary Pi install the following
- Mosquito https://www.instructables.com/Installing-MQTT-BrokerMosquitto-on-Raspberry-Pi/ 
- Node-Red https://nodered.org/docs/getting-started/raspberrypi
- InfluxDB https://simonhearne.com/2020/pi-influx-grafana/
- Grafana https://simonhearne.com/2020/pi-influx-grafana/

## Node-Red Flow
![WeatherPi_Flow_20201106_2219](https://user-images.githubusercontent.com/5247403/100123009-fa45e980-2e71-11eb-98a8-1149db2b5cda.png)

## Wiring Diagram
![WeatherStation PemaProto Half_bb](https://user-images.githubusercontent.com/5247403/100123667-ad164780-2e72-11eb-8061-ee044636ece5.png)

## Grafana Dashboard
![Grafana Dashboard 2020-11-09 at 08 37 16](https://user-images.githubusercontent.com/5247403/98518170-f194c700-2266-11eb-9a6c-9aa087cb88b6.png)
