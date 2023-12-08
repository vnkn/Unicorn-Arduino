from urllib.request import urlopen

response = urlopen('https://lab.wolframcloud.com/objects/f9ac8238-ff37-4fa4-a750-5f1286b41026')
data = response.read()
print(data)

import serial
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)  # open serial port
import time
time.sleep(2)

data2 = data
while(True):
	response = urlopen('https://lab.wolframcloud.com/objects/f9ac8238-ff37-4fa4-a750-5f1286b41026')
	data2 = response.read()

	if (data2 != data):
		ser.write(data2)
		data = data2 
	    # write a string

print(ser.name)         # check which port was really used
ser.write(b'one')     # write a string
print("hi");
#ser.close()             # close port
