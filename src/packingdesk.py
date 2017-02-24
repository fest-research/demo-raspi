# -*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import urllib2
import random

cloudUrl = "http://35.187.21.121:8080/api/v1/proxy/namespaces/default/services/demo/push/"

GPIO.setmode(GPIO.BCM)
rot = 0
gruen = 1
taster = 2
Desk = [18, 23, 25]
GPIO.setup(Desk[rot], GPIO.OUT, initial=False)
GPIO.setup(Desk[gruen], GPIO.OUT, initial=False)
GPIO.setup(Desk[taster], GPIO.IN)
print("startingdemo app ")

try:
    while True:
        if GPIO.input(Desk[taster]):
            GPIO.output(Desk[rot], True)
            time.sleep(10)
            GPIO.output(Desk[gruen], True)
            GPIO.output(Desk[rot], False)
            time.sleep(2)
            GPIO.output(Desk[gruen], False)
            orderId = random.randint(1000000, 9000000)
            message = "Order%20" + str(orderId) + "%20shipped"
            print("Sending msg: {}".format(cloudUrl + message))
            urllib2.urlopen(cloudUrl + message).read()
	else:
	    time.sleep(0.1)


except KeyboardInterrupt:
    GPIO.cleanup()
