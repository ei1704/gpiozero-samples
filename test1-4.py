from gpiozero import PWMLED
from time import sleep

led1=PWMLED(23)

led1.value=0
value=0

while True:
    sleep(0.5)
    value+=0.2
    if value==1.2:
        value=0
    led1.value=value