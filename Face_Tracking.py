#!/usr/bin/python3
# Need Ezblock librairies from sunfounder github or an image os install from https://ezblock.cc/download/index.html
# It's a modified example file from Sunfounder. 

import sys
sys.path.append(r'/opt/ezblock')
from vilib import Vilib
from ezblock import WiFi
from ezblock import constrain
from ezblock import PWM
from ezblock import Servo

xVal = None
yVal = None
panAngle = None
tiltAngle = None

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
panAngle = 0
tiltAngle = 0
WiFi().write('Country', 'ssid', 'ssidPass')

pwm_P0 = PWM("P0")

pwm_P1 = PWM("P1")


def forever():
    global xVal, yVal, panAngle, tiltAngle
    xVal = Vilib.human_detect_object('x')
    yVal = Vilib.human_detect_object('y')
    if (Vilib.human_detect_object('number')) >= 1:
        if xVal == -1:
            panAngle = panAngle + 1
        elif xVal == 1:
            panAngle = panAngle - 1
        if yVal == -1:
            tiltAngle = tiltAngle + 1
        elif yVal == 1:
            tiltAngle = tiltAngle - 1
        panAngle = constrain(panAngle, -90, 90)
        tiltAngle = constrain(tiltAngle, -45, 25)
        Servo(pwm_P0).angle(panAngle)
        Servo(pwm_P1).angle(tiltAngle)

if __name__ == "__main__":
    while True:
        forever()  
