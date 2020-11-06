# WeatherPi
Raspberry Pi based wether station

<h2>Install Process</h2>
<ul>
 <li>New image of Raspian Lite with no applications or desktop</li>
 <li>Enable SSH</li>
 <li>Enable I2C</li>
 <li>Install Node.JS and NPM https://www.instructables.com/Install-Nodejs-and-Npm-on-Raspberry-Pi/ </li>
 <li>
  
</ul>


•	 sudo apt install build-essential git first to ensure npm is able to build any binary modules it needs to install.
•	Install pip
•	Install VEML6075 library https://github.com/pimoroni/veml6075-python
•	Install I2S mic https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test 
o	pip install sounddevice==0.3.15
•	Install Enviro Libraries https://github.com/pimoroni/enviroplus-python 
•	Install NodeRed https://nodered.org/docs/getting-started/local 
•	Install Nodes
o	DHt22
o	Node-Red-Dashboard
o	node-red-node-pi-mcp3008
o	node-red-contrib-python-function
o	node-red-contrib-counter
o	node-red-contrib-bme280
o	node-red-contrib-msg-speed
•	On Primary Pi
o	Install Mosquito (MQTT Broker)
o	Install NodeRed
o	Install InfluxDB
o	Install Grafana
•	https://gpiozero.readthedocs.io/en/stable/installing.html 

