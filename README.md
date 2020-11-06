# WeatherPi
Raspberry Pi based wether station

<h2>Install Process</h2>
<ul>
 <li>New image of Raspian Lite with no applications or desktop</li>
 <li>Enable SSH</li>
 <li>Enable I2C</li>
 <li>Install Node.JS and NPM https://www.instructables.com/Install-Nodejs-and-Npm-on-Raspberry-Pi/ sudo apt install build-essential git first to ensure npm is able to build any binary modules it needs to install</li>
 <li>Install pip</li>
 <li>Install VEML6075 library https://github.com/pimoroni/veml6075-python</li>
 <li>Install I2S mic https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test</li>
 <li>pip install sounddevice==0.3.15</li>
 <li>Install Enviro Libraries https://github.com/pimoroni/enviroplus-python</li>
 <li>Install NodeRed https://nodered.org/docs/getting-started/local </li>
</ul>
<h3>Install Nodes</h3>
<ul>
 <li>DHt22</li>
 <li>Node-Red-Dashboard</li>
 <li>node-red-node-pi-mcp3008</li>
 <li>node-red-contrib-python-function</li>
 <li>node-red-contrib-counter</li>
 <li>node-red-contrib-bme280</li>
 <li>node-red-contrib-msg-speed</li>
</ul>



•
o	
o	
o	
o	node-red-contrib-msg-speed
•	On Primary Pi
o	Install Mosquito (MQTT Broker)
o	Install NodeRed
o	Install InfluxDB
o	Install Grafana
•	https://gpiozero.readthedocs.io/en/stable/installing.html 

