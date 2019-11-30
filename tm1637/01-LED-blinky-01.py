from gpiozero import LED
from time import sleep

led1 = LED(23)

while True:
    led1.on()
    sleep(0.35)
    led1.off()
    sleep(0.15)
