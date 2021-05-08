import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)


s.write(bytes("/LEDControl/run 1 1\r", 'UTF-8'))


s.close()