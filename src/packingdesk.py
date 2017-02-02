# -*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import urllib2
import random

cloudUrl = "http://104.155.11.172:8080/api/v1/proxy/namespaces/default/services/demo/push/"

GPIO.setmode(GPIO.BCM)
rot = 0
gruen = 1
taster = 2
Desk = [18, 23, 25]
GPIO.setup(Desk[rot], GPIO.OUT, initial=False)
GPIO.setup(Desk[gruen], GPIO.OUT, initial=False)
GPIO.setup(Desk[taster], GPIO.IN)
print("starting")

try:
    while True:
        if GPIO.input(Desk[taster]):
            GPIO.output(Desk[rot], True)
            time.sleep(10)
            GPIO.output(Desk[gruen], True)
            GPIO.output(Desk[rot], False)
            time.sleep(15)
            GPIO.output(Desk[gruen], False)
            orderId = random.randint(1000000, 9000000)
            message = "Order%20" + str(orderId) + "%20shipped"
            print("Sending msg: {}".format(cloudUrl + message))
            urllib2.urlopen(cloudUrl + message).read()


except KeyboardInterrupt:
    GPIO.cleanup()
