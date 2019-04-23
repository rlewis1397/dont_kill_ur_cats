
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

def motion(channel):
	print('Motion detected')
	# node server to call aromatherapy diffuser to turn off 
	time.sleep(2)

try:
	GPIO.add_event_detect(18, GPIO.RISING, callback=motion)
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print('Code interrupted')
	GPIO.cleanup()
