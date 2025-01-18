import requests
import RPi.GPIO as GPIO
import time



pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def downstairs_bedroom(channel):
        requests.get("https://api-v2.voicemonkey.io/trigger?token=1eaef0c009d4493c7f56ed423d8664f9_a864915ae61a09310edca8249aebf5c2&device=downstairs-bedroom")

GPIO.add_event_detect(pin, GPIO.FALLING, callback=downstairs_bedroom, bouncetime=100)

try:
        while True:
                time.sleep(0.01)
except KeyboardInterrupt:
        GPIO.cleanup()