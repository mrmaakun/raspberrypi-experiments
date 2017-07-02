import RPi.GPIO as GPIO
import time

PUSH_BUTTON = 40

#Set to use pin numbers on the board
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
	while True:
		button_input = GPIO.input(PUSH_BUTTON)
		if button_input == False:
			print ("Button Pressed")
			time.sleep(0.2)

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
