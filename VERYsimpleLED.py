#!/usr/bin/python3
"""
Turning LED ON via SWITCH
Tayla Anthony
Readjust this Docstring as follows:
Names: Tayla Anthony
Student Number: ANTTAY001
Prac: 1*
Date: 24/07/19
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep

lightPin = 23
buttonPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

try:
	while True:

		GPIO.output(lightPin, not GPIO.input(buttonPin))
		sleep(1)

except KeyboardInterrupt:
	print("Exiting gracefully")

	# Turn off your GPIOs here
	GPIO.cleanup()
except:
	print("Some other error occurred")

finally:
	GPIO.output(lightPin, False)
	GPIO.cleanup()





