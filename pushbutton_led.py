import RPi.GPIO as GPIO
import time

print ("Blinking LEDs")

# LED state variable
blinking = True

# Use constants to map the pin number to its corresponding color
RED_LED = 29
YELLOW_LED = 31
GREEN_LED = 33
PUSH_BUTTON = 40
SENSOR = 38

def blink(pin):
	if blinking == True:
		GPIO.output(pin,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(pin,GPIO.LOW)
		time.sleep(.1)
	return

def button_press(channel):
	print "Button press detected."
	global blinking 
	blinking = not blinking
	if blinking == True:
		print("Run LEDs")
	else:
		print("Stop LEDs")


GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(PUSH_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(PUSH_BUTTON, GPIO.FALLING, callback=button_press, bouncetime=300)

try:
	while True:
		if blinking == True:
			blink(RED_LED)
			blink(YELLOW_LED)
			blink(GREEN_LED)
			blink(YELLOW_LED)

except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
