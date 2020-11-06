#!/usr/bin/env python

import time
import veml6075
import smbus
import json
bus = smbus.SMBus(1)

# Create VEML6075 instance and set up
uv_sensor = veml6075.VEML6075(i2c_dev=bus)
uv_sensor.set_shutdown(False)
uv_sensor.set_high_dynamic_range(False)
uv_sensor.set_integration_time('100ms')

# Do the Thing
uva,uvb = uv_sensor.get_measurements()
uv_comp1, uv_comp2 = uv_sensor.get_comparitor_readings()
uv_indices = uv_sensor.convert_to_index(uva, uvb, uv_comp1, uv_comp2)

x = {
    "uva": uva,
    "uvb": uvb,
    "comp1":uv_comp1,
    "comp2":uv_comp2,
    "uva_index":round(uv_indices[0],2),
    "uvb_index":round(uv_indices[1],2),
    "avg_uv_index":round(uv_indices[2],2)
}

# Convert to JSON: 
y = json.dumps (x)

# Print Info
print (y)