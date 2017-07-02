import RPi.GPIO as GPIO
import time

SENSOR_PIN = 38

#Set to use pin numbers on the board
GPIO.setmode(GPIO.BOARD)

GPIO.setup(SENSOR_PIN, GPIO.IN)


try:
	while True:
		sensor_input = GPIO.input(SENSOR_PIN)
		if sensor_input == True:
			print ("Person Detected")
			time.sleep(0.2)

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
