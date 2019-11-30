import tm1637
from time import sleep

display = tm1637.TM1637(CLK=20,DIO=21,brightness=7)

display.Clear()

#a=b=c=d=0

#data = [a,b,c,d]

#display.Show(data)
#n=20
i=0
n=60

for i in range(n):
  display.ShowRoute(i%6)
  sleep(0.05)


#while True:
#  d=int(i%10)
#  c=int(i/10)
#  c=int(c%10)
#  b=int(i/100)
#  b=int(b%10)
#  a=int(i/1000)
#  a=int(a%10)
#  sleep(0.1)
#  data = [a,b,c,d]
#  display.Show(data)
#  i+=1