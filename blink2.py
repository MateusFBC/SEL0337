from gpiozero import LED

pin = LED(18)

while 1:
	pin.on()
