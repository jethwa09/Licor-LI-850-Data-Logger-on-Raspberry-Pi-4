
import datetime
import time
from time import sleep
import serial
import re
from datetime import datetime
import csv



tty1= serial.Serial(port='/dev/serial1', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)


print("tty1",tty1)
co2_pattern = r'<co2>(.*?)</co2>'
h2o_pattern = r'<h2o>(.*?)</h2o>'
celltemp_pattern = r'<celltemp>(.*?)</celltemp>'


while True:
	time.sleep(1)
	sensor_data=tty1.readline()
	print (sensor_data)
	print ("_______________________________")
	string = sensor_data.decode('utf-8')
	co2_match = re.search(co2_pattern, string)
	if co2_match:
		co2_value = co2_match.group(1)
		co2_value_float = float(co2_value)
	else:
		co2_value_float = "N/A_CO2"
	h2o_match = re.search(h2o_pattern, string)
	if h2o_match:
		h2o_value = h2o_match.group(1)
		h20_value_float = float(h2o_value)
	else:
		h2o_value_float = "N/A_H2O"

	celltemp_match = re.search(celltemp_pattern, string)
	if celltemp_match:
		celltemp_value = celltemp_match.group(1)
		celltemp_value_float = float(celltemp_value)
	else:
		celltemp_value_float = "N/A_Temo"
	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"\r| CO2 | Cell Temp | Date & Time", end="")
	print(f"\r| {co2_value_float:^6}  | {celltemp_value_float:^11} | {current_time}", end="\n")
	with open('data.csv', mode='a', newline='') as file:
		writer = csv.writer(file)
		writer.writerow([co2_value_float, celltemp_value_float, current_time])
	#time.sleep(1)
