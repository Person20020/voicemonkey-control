import requests
import RPi.GPIO as GPIO
import time



pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def downstairs_bedroom(channel):
        requests.get("https://api-v2.voicemonkey.io/trigger?token=<api key here>&device=downstairs-bedroom")

GPIO.add_event_detect(pin, GPIO.FALLING, callback=downstairs_bedroom, bouncetime=100)

try:
        while True:
                time.sleep(0.01)
except KeyboardInterrupt:
        GPIO.cleanup()
