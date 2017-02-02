# -*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import urllib2

# load drivers
# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')
temp_sensor = "/sys/bus/w1/devices/28-8000001f29ca/w1_slave"

GPIO.setmode(GPIO.BCM)
rot = 0
gruen = 1
taster = 2

Desk = [18, 23, 25]
GPIO.setup(Desk[rot], GPIO.OUT, initial=False)
GPIO.setup(Desk[gruen], GPIO.OUT, initial=False)
GPIO.setup(Desk[taster], GPIO.IN)
print("starting")


def measureTemp():
    with open(temp_sensor) as f:
        filecontent = f.read()
        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000
        return temperature


try:
    while True:
        if GPIO.input(Desk[taster]):
            GPIO.output(Desk[rot], True)
            print(measureTemp())
            while measureTemp() <= 25:
                time.sleep(0.05)

            GPIO.output(Desk[gruen], True)
            GPIO.output(Desk[rot], False)
            time.sleep(2)
            GPIO.output(Desk[gruen], False)
            urllib2.urlopen("http://www.heise.de").read()
except KeyboardInterrupt:
    GPIO.cleanup()
