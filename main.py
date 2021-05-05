# -*- coding: utf-8 -*-
from gpiozero import Button
from picamera import Picamera
import datetime
from signal import pause
from time import sleep

button = Button(2)# GPIO2에 연결된 버튼
camera = Picamera()

def capture():
    now = datetime.datetime.now()
    sleep(5)
    camera.capture('/home/pi/%s.jpg' % now)
    
button.when_pressed = capture

pause()
