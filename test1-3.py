from gpiozero import LED,Button
from signal import pause

led1=LED(23)
button1=Button(24,pull_up=False)

button1.when_pressed=led1.on
button1.when_released=led1.off

pause()