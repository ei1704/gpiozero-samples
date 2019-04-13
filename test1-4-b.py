from gpiozero import PWMLED
from time import sleep
from gpiozero import Button

button = Button(24,pull_up=False)

led1 = PWMLED(23)

led1.value = 0

while True:

    if button.is_pressed:
        break
    led1.value += 0.2
    sleep(0.5)
    if led1.value==1:
        led1.value=0
    

