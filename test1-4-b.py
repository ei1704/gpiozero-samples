from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(23)

led1.value = 0

while True:
    led1.value += 0.2
    sleep(0.5)
    if led1.value==1:
        led1.value=0
