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

lightPin = 27
butINC = 25
butDEC= 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(butINC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butDEC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin, False)

def my_callback_one(butINC):
    print('This is a edge event callback function!')
    print('Edge detected on channel 25')
    print('This is run in a different thread to your main program')
    

def my_callback_two(butDEC):
    print('This is a edge event callback function!')
    print('Edge detected on channel 16')
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(butINC, GPIO.FALLING, callback=my_callback_one, bouncetime=200)
GPIO.add_event_detect(butDEC, GPIO.FALLING, callback=my_callback_two, bouncetime=200)

def main():
    if GPIO.event_detected(butINC):
        GPIO.output(lightPin, True)
        sleep(1)
        
    if GPIO.event_detected(butDEC):
        GPIO.output(lightPin,False)
        sleep(1)

if __name__ == "__main__":
# Make sure the GPIO is stopped correctly  
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")




