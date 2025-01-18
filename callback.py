import RPi.GPIO as GPIO
import time
import requests

entries = {
    "pins": [13, 19, 26],
    "ids": ["kojis-room", "downstairs-bathroom", "lamp"]
}

token = "1eaef0c009d4493c7f56ed423d8664f9_a864915ae61a09310edca8249aebf5c2"
url = "https://api-v2.voicemonkey.io/trigger?token=" + token + "&device="

def my_callback(channel):
    print(f"Interrupt detected on channel {channel}")
    index = entries["pins"].index(channel)
    
    print(url + entries["ids"][index])
    requests.get(url + entries["ids"][index])


GPIO.setmode(GPIO.BCM)

print("Setting up GPIO pins...")
for pin in entries["pins"]:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Adding event detection for both pins...")
for pin in entries["pins"]:
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=my_callback, bouncetime=200)


try:
    print("Waiting for interrupts...")
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n")
    print("Cleaned up GPIO")
