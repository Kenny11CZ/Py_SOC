#!/usr/bin/python
__author__ = 'Kenny'

import RPi.GPIO as GPIO
import time

LED_ON = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ON, GPIO.OUT)
GPIO.output(LED_ON, False)
time.sleep(1)
GPIO.output(LED_ON, True)
time.sleep(10)
GPIO.output(LED_ON, False)
time.sleep(1)
