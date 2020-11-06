# WeatherPi
Raspberry Pi based wether station

<h2>Install Process</h2>
<ul>
 <li>New image of Raspian Lite with no applications or desktop</li>
 <li>Enable SSH</li>
 <li>Enable I2C</li>
 </ul>
 <h3>Install the following</h3>
 <ul>
 <li>Node.JS and NPM https://www.instructables.com/Install-Nodejs-and-Npm-on-Raspberry-Pi/ sudo apt install build-essential git first to ensure npm is able to build any binary modules it needs to install</li>
 <li>pip</li>
 <li>VEML6075 library https://github.com/pimoroni/veml6075-python</li>
 <li>I2S mic https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-test</li>
 <li>pip install sounddevice==0.3.15</li>
 <li>Pimoroni Enviro Libraries https://github.com/pimoroni/enviroplus-python</li>
 <li>Node-Red https://nodered.org/docs/getting-started/local </li>
</ul>

### Install the following Nodes
- DHt22
- Node-Red-Dashboard
<ul>
 <li>node-red-node-pi-mcp3008</li>
 <li>node-red-contrib-python-function</li>
 <li>node-red-contrib-counter</li>
 <li>node-red-contrib-bme280</li>
 <li>node-red-contrib-msg-speed</li>
 <li>node-red-contrib-msg-speed</li>
</ul>
<h3>On Primary Pi install the following</h3>
<ul>
 <li>Mosquito</li>
 <li>Node-Red</li>
 <li>InfluxDB</li>
 <li>Grafana</li>
 </ul>

## Node-Red Flow
![WeatherPi_Flow_20201106_2219](https://user-images.githubusercontent.com/5247403/98422214-fdc02f00-2082-11eb-8a97-c4378d4a1931.png)

## Wiring Diagram
![WeatherStation PemaProto Half_bb](https://user-images.githubusercontent.com/5247403/98422125-cd789080-2082-11eb-8f47-790ee3bd5da4.png)
