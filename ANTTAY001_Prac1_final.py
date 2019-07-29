#!/usr/bin/python3
"""
Prac 1: Final
Tayla Anthony
Readjust this Docstring as follows:
Names: Tayla Anthony
Student Number: ANTTAY001
Prac: 1
Date: 28/07/19
"""
# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep #sleep function to create delays
import itertools

#GPIO setup
chan_list= (27,22,17) #LED pins
butINC = 25 #Up button pin
butDEC = 16 #Down button pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(butINC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(butDEC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.output(chan_list, False) #all LEDS are off initially

global counter 
counter = 0 #counter to index through list of binary values

#Creating list of binary numbers
n=3
lst = list(itertools.product([0, 1], repeat=n))

#Callback functions for switches
def my_callback_one(butINC): #callback function when pushing increment button
    global counter
    counter += 1 #move forward in list of binary numbers
    if counter<0: #check that counter isnt negative number or 0
        counter += 8
    if counter==8:
        counter=0

    GPIO.output(chan_list,lst[counter]) #output binary value to LEDs
    sleep(.2) # 0.2 sec delay
    print('Up')

def my_callback_two(butDEC): #callback function when decrement button is pushed
    global counter
    counter -= 1 
    if counter<0:
        counter += 8
    if counter==8:
        counter=0

    GPIO.output(chan_list,lst[counter])  #output binary value to LEDs
    sleep(.2) #0.2 sec delay
    print('Down')

#Interrupts and debounce
GPIO.add_event_detect(butINC, GPIO.FALLING, callback=my_callback_one, bouncetime=200)
GPIO.add_event_detect(butDEC, GPIO.FALLING, callback=my_callback_two, bouncetime=200)

def main():
    pass

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
            

            
        