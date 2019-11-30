from gpiozero import DistanceSensor
from time import sleep
import tm1637

display = tm1637.TM1637(CLK=20,DIO=21,brightness=7)

display.Clear()

MAX_DISTANCE=2
sensor = DistanceSensor(echo=24,trigger=23,max_distance=MAX_DISTANCE)

#while True:
#  print(sensor.distance*100)
#  sleep(0.5)

a=b=c=d=0
data = [a,b,c,d]
display.Show(data)

while True:
  value=int(sensor.distance*100)
  d=int(value%10)
  c=int(value/10)
  c=int(c%10)
  sleep(0.01)
  data = [a,b,c,d]
  display.Show(data)