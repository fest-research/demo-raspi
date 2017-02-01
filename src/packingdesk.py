#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import urllib2


GPIO.setmode(GPIO.BCM)
rot = 0; gruen = 1; taster=2

Desk=[18,23,25]
GPIO.setup(Desk[rot], GPIO.OUT, initial=False)
GPIO.setup(Desk[gruen], GPIO.OUT, initial=False)
GPIO.setup(Desk[taster], GPIO.IN)
print("starting")


def measureTemp():
    file = open(temp_sensor)
    filecontent = file.read()
    file.close()
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000
    return(temperature)




try:
	while True:
		if GPIO.input(Desk[taster])==True:
			GPIO.output(Desk[rot], True)
			time.sleep(10)			
			GPIO.output(Desk[gruen], True); GPIO.output(Desk[rot], False)
			time.sleep(2)
			GPIO.output(Desk[gruen], False)
			urllib2.urlopen("http://www.heise.de").read()
except KeyboardInterrupt:
	GPIO.cleanup()


