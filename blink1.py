from gpiozero import LED
from time import sleep

pin = LED(23)

while 1:
	pin.on()
	sleep(1)
	pin.off()
	sleep(1)
